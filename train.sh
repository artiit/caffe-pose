#!/bin/bash

build/tools/caffe train -gpu 0 -solver models/limb/solver.prototxt  2>&1 | tee -a data/flic/test/1/train.log


#build/tools/caffe train -weights data/flic/nets/heatmap-flic-fusion/fusion6/fusion6_iter_40000.caffemodel -gpu 0 -solver models/heatmap-flic-fusion/idea1/solver.prototxt 2>&1 | tee -a data/flic/nets/full_label/train.log
# -weights data/flic/nets/flic_15joints/conv8/flic_15_conv8_iter_20000.caffemodel 

