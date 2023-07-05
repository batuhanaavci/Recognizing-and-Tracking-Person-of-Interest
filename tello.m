
global files;
folder = "frame/3/";
files = dir(folder);
count = numel(files)-2;
disp(sprintf("%d",count)+" Frame Recorded");
%%
joyNode = ros2node("/joy_node");
joySub = ros2subscriber(joyNode,"/joy",@joyCallback);
imgNode = ros2node("/tello_driver");
imgSub = ros2subscriber(imgNode,"image_raw");
pause(2)

global button;
global state;
state = 1;


frame = count-1;

while 1
    pause(0.1);

    if state == 2
        imgMsg = receive(imgSub,10);
        img = rosReadImage(imgMsg);
        %imshow(img)
        %subImage = img(24:3:695, 32:4:927,:); %224x224x3 image
        imwrite(img,folder+sprintf("%05d",frame)+".jpg");
        frame=frame+1;
    end
        
end

function joyCallback(joyData)
    global button;
    button = joyData.buttons(1);
    global state;

    switch state
        case 1 %off 
            if button ==1
                clc;
                disp("Recording Started...")
                state =2;
            end
        case 2 %on           
            if button ==1
                clc;
                disp("Recording Stopped...")
                state = 1;
            end
    end

end