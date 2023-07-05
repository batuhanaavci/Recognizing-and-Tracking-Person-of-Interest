global files;
folder = "frame/3/";
files = dir(folder);,
count = numel(files)-2;
resizedFolder = "frame/resized_3/";

for frame=1:count
    img = imread(folder+sprintf("%05d",frame)+".jpg");
    subImage = img(24:3:695, 32:4:927,:);
    imwrite(subImage,resizedFolder+sprintf("%05d",frame)+".jpg");
end