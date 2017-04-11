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
  
  #add for heatmap
  training_heatmap_loss = []  
  training_fusion_loss = []
#  training_fusion2_loss = []


  check_test = False
  for line in f:

    if check_test:
      if 'Test net output' in line and 'loss_fusion' in line:
        sumloss = float(line.strip().split(' ')[-2])
      #if 'Test net output' in line and 'loss_fusion2' in line:
        #sumloss += float(line.strip().split(' ')[-2])
      if 'Test net output' in line and 'loss_heatmap' in line:
        test_loss.append(float(line.strip().split(' ')[-1])+sumloss)
        check_test2 = False
    if '] Iteration ' in line and 'loss = ' in line:
      arr = re.findall(r'ion \b\d+\b,', line)
      training_iterations.append(int(arr[0].strip(',')[4:]))
      training_loss.append(float(line.strip().split(' = ')[-1]))
    
    # add for heatmap
    if 'Train net output #0: loss_fusion' in line:
      training_fusion_loss.append(float(line.strip().split(' ')[-2]))
    #if 'Train net output #1: loss_fusion2' in line:
      #training_fusion2_loss.append(float(line.strip().split(' ')[-2]))
    if 'Train net output #1: loss_heatmap' in line:
      training_heatmap_loss.append(float(line.strip().split(' ')[-1]))

    ##
    if '] Iteration ' in line and 'Testing net' in line:
      arr = re.findall(r'ion \b\d+\b,', line)
      test_iterations.append(int(arr[0].strip(',')[4:]))
      check_test = True

  print 'train iterations len: ', len(training_iterations)
  print 'train loss len: ', len(training_loss)
  print 'heat loss len: ', len(training_heatmap_loss)
  print 'fusion loss len: ', len(training_fusion_loss)
  #print 'fusion2 loss len: ', len(training_fusion2_loss)
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
  p2, = host.plot(training_iterations,training_heatmap_loss,label= "heatmap loss")
  p3, = host.plot(training_iterations,training_fusion_loss, label = "fusion loss")
  p4, = host.plot(test_iterations, test_loss, label="test loss")
  #p5, = host.plot(training_iterations,training_fusion2_loss, label = "fusion2 loss")

  host.legend(loc=2)

  host.axis["left"].label.set_color(p1.get_color())

  plt.draw()
  plt.show()

