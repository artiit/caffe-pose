import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
import sys
import argparse
import re
from pylab import figure, show, legend, ylabel

from mpl_toolkits.axes_grid1 import host_subplot


if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='makes a plot from Caffe output')
  parser.add_argument('output_file', help='file of captured stdout and stderr')
  args = parser.parse_args()
  
  f = open(args.output_file, 'r')

  training_iterations = []
  training_loss = []

  test_iterations = []
  test_loss = []


  check_test = False
  for line in f:

    if check_test:
      if 'Test net output' in line and 'loss_heatmap' in line:
        test_loss.append(float(line.strip().split(' ')[-2]))
        check_test2 = False
    if '] Iteration ' in line and 'loss = ' in line:
      arr = re.findall(r'ion \b\d+\b,', line)
      training_iterations.append(int(arr[0].strip(',')[4:]))
      training_loss.append(float(line.strip().split(' = ')[-1]))
    
    if '] Iteration ' in line and 'Testing net' in line:
      arr = re.findall(r'ion \b\d+\b,', line)
      test_iterations.append(int(arr[0].strip(',')[4:]))
      check_test = True

  print 'train iterations len: ', len(training_iterations)
  print 'train loss len: ', len(training_loss)
  print 'test loss len: ', len(test_loss)
  print 'test iterations len: ', len(test_iterations)

  f.close()
#  plt.plot(training_iterations, training_loss, '-', linewidth=2)
#  plt.show()
  
  host = host_subplot(111)#, axes_class=AA.Axes)
  plt.subplots_adjust(right=0.75)

  par1 = host.twinx()

  host.set_xlabel("iterations")
  host.set_ylabel("log loss")
  
  p1, = host.plot(training_iterations, training_loss, label="training loss")
  p2, = host.plot(test_iterations, test_loss, label="test loss")

  host.legend(loc=2)

  host.axis["left"].label.set_color(p1.get_color())

  plt.draw()
  plt.show()

