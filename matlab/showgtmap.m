height = 64;
width = 64;
sigma = 3.5;
joints = [30,22;19,46;40,43;15,41;37,37;21,28;34,30];
label = zeros(64);
for indx = 1:7
    for i = 0:width-1
        for j = 1:height
            gaussian = exp(-0.5*((i-joints(indx,1))^2+(j-joints(indx,2))^2)*(1 / sigma)^2.0);
            label(i*width + j) = label(i*width+j)+gaussian;
        end
    end
end
label = label./(max(max(label)))
imshow(label)