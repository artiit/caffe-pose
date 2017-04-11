% Options

opt.visualise = true;		% Visualise predictions?
opt.useGPU = true; 			% Run on GPU
opt.dims = [256 256]; 		% Input dimensions (needs to match matlab.txt)

opt.numJoints = 14; 			% Number of joints

opt.layerName = 'conv6_fusion'; % Output layer name

%opt.modelDefFile = '../../models/limb/lsp_2limb_matlab.prototxt'; % Model definition
opt.modelDefFile = '../../models/limb/lsp_test3_matlab.prototxt';

opt.modelFile = '../../data/kinect/mix1/mix1_iter_13000.caffemodel';
%opt.modelFile = '../../data/flic/test/limb/test3_iter_40000.caffemodel'; % Model weights
%opt.modelFile = '../../data/lsp/test1/2limb/2limb_iter_60000.caffemodel';
%opt.modelFile = '/home/ai/limb_iter_40000.caffemodel';
%opt.modelFile = '../../data/lsp/test/limb_old/test3_iter_80000.caffemodel'
%opt.modelFile = '../../data/test/test_iter_10000.caffemodel'
% Add caffe matlab into path
addpath('../')

% Image input directory
%opt.inputDir = '/home/ai/data/heatmap_data/kinect_data/test/mix/images/';
opt.inputDir = '/home/ai/data/heatmap_data/kinect_data/test/v3/images/'
%opt.inputDir = '/home/ai/images/';
%opt.inputDir = 'flic_test/'
%opt.inputDir = 'lsp_test/'
% Create image file list
imInds = 1535;
for ind = 1:numel(imInds); files{ind} = ['im' num2str(imInds(ind)) '.jpg']; end

% Apply network
joints = applyNet(files, opt)

%%
% processHeatmap  need to change while change the model.