load("yolov2_vgg19_aug.mat")
node1 = ros2node('node1')
imgNode = ros2node("/tello_driver");
imgSub = ros2subscriber(imgNode,"image_raw");
dataPub = ros2publisher(node1,"/faces","std_msgs/String");
dataMsg = ros2message(dataPub);
pause(0.5)
imgMsg = receive(imgSub,10);
img = rosReadImage(imgMsg);

while 1

    pause(0.01);
    imgMsg = receive(imgSub,10);
    img = rosReadImage(imgMsg);
    subImage = imresize(img,[224 224]);
    [faces.boxes,faces.scores,faces.labels] = detect(detector,subImage);
    
    faces.boxes(:,1) = floor(faces.boxes(:,1)*4.2);
    faces.boxes(:,2) = floor(faces.boxes(:,2)*3.5);
    faces.boxes(:,3) = floor(faces.boxes(:,3)*4);
    faces.boxes(:,4) = floor(faces.boxes(:,4)*2.8);

    faces_data = jsonencode(faces);
    dataMsg.data = faces_data;
    send(dataPub,dataMsg)

end

