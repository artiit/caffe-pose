% tranfer txt label file to label.mat
m = load('lsptest.txt');
labels = reshape(m',2,14,1000);
save('lsplabel.mat','labels');
