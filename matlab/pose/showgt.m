% takes 2.5 seconds to load 21K element annotation struct
load fliclabel.mat
imgdir = 'flic_test';
% display a image
img = imread([imgdir,'/im6.png']);
cla, imagesc(img), axis image, hold on
label = labels(:,:,6);


% display all the labeled joints; median of 5 annotations by mechanical turk
plot(label(1,[5,7]),label(2,[5,7]),'go-','linewidth',3)
plot(label(1,[4,6]),label(2,[4,6]),'mo-','linewidth',3)
plot(label(1,[3,5]),label(2,[3,5]),'bo-','linewidth',3)
plot(label(1,[2,4]),label(2,[2,4]),'co-','linewidth',3)
