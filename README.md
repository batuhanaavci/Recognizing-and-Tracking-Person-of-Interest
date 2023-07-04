# Recognizing and Tracking Person of Interest: 
MathWorks Excellence in Innovation Project 214 Solution

MATLAB-ROS2-Python implementation of the system architecture in the following paper:
~~~
H. E. Dursun, E. C. Güven, B. Avcı, T. Kumbasar, 2023. Recognizing and Tracking Person of Interest: A Real-Time Efficient Deep Learning based Method for Quadcopters, International Conference on Recent Advances in Air and Space Technologies, Istanbul, Turkey.
~~~
A Real-Time Efficient Deep Learning based Method for Quadcopters

Welcome to the GitHub repository for our project, which extends the work presented in our conference paper titled "Recognizing and Tracking Person of Interest: A Real-Time Efficient Deep Learning based Method for Quadcopters." This repository serves as a comprehensive resource for anyone interested in exploring our project and contributing to its development.

## Project Overview
In this project, we aim to address the challenge of recognizing and tracking a person of interest using quadcopters. Our goal is to develop a real-time, efficient deep learning-based method that enables quadcopters to autonomously detect and track individuals in various scenarios. By leveraging the power of MATLAB and Simulink, we strive to provide a solution with industry relevance and societal impact.

### Abstract
The recognition and tracking of a person of interest is a crucial task in applications such as search and rescue, security, and surveillance. This thesis presents a distributed system architecture that leverages ROS2 (Robot Operating System 2) and deep learning techniques to develop a real-time efficient method for recognizing and tracking a person of interest using a quadcopter. The system utilizes a deep learning model to recognize persons in snapshots from the quadcopter's camera and generates reference velocity signals for the drone's flight control system to track the person of interest. The proposed architecture is evaluated in cluttered and complex environments, demonstrating its effectiveness in real-world scenarios.

[![IMAGE ALT TEXT](https://img.youtube.com/vi/i7bYXnRy8Vc/0.jpg)](https://www.youtube.com/watch?v=i7bYXnRy8Vc&t=7s "Video Title")



## Key Features and Objectives
- **Real-time Person Recognition**: We employ advanced deep learning techniques to accurately identify individuals in real-time.
- **Efficient Tracking Algorithm**: Our project focuses on developing an efficient tracking algorithm that enables quadcopters to maintain visual contact with the person of interest.
- **Robust Performance**: We aim to create a solution that can handle various environmental conditions, such as changes in lighting, occlusions, and complex backgrounds.
- **Integration with Quadcopter Systems**: Our method is designed to be easily integrated with existing quadcopter systems, facilitating practical implementation and deployment.

![IMAGE ALT TEXT](https://github.com/batuhanaavci/Recognizing-and-Tracking-Person-of-Interest/blob/main/images/image.png)

## Dependencies
ROS2 Foxy
Matlab R2022b with Deep Learning Toolbox
Python 3.8.13 with required libraries (specified in the code)

## Getting Started
To get started with our project, please refer to the following steps:

1. Clone the repository to your local machine using the command:
`https://github.com/enescanguven/tello_ros.git` and follow instructions to download Ros2 and DJI Tello package and run.
2. Clone the repository to your local machine using the command: `https://github.com/batuhanaavci/faster_rcnn_face_recog_drone.git`
3. Install MATLAB and Simulink, ensuring that you have the necessary toolboxes and dependencies mentioned in the documentation.
4. Navigate to the relevant directories within the `tracking_control` folder to explore the source code for tracking algorithm and run followings in terminal.
    ~~~
    source /opt/ros/foxy/setup.bash
    python3 tracking.py
    ~~~
5. For the matlab recognition part real-time inference and matlab-ros2 communication, navigate to `face_recognition/real-time` folder and run the `ros-detect-node.m` matlab file.

## Train your Own Model
To train your own model, please refer to the following steps:

1. Collect the data set in accordance with the information provided in  `face_recognition/training`
2. Train your model following the instructions given  in `face_recognition/training/yolov.mlx`
3. Export your new model to file system and move it to the `face_recognition/real-time` folder
4. Edit the `face_recognition/real-time/ros_detect_node.m` file with you new DL models name.
5. Finally run the code.

## Contributions
We appreciate contributions from the community to improve our project. 

## License
This project is licensed under the [MIT License](

## Contact Information
For any questions, suggestions, or feedback, please contact us at:

- Name: Batuhan Avci
- Email: avcib19@itu.edu.tr

## Resources

* [Tello User Manual 1.4](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20User%20Manual%20v1.4.pdf)
* [SDK 1.3](https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf)
for Tello, see the errata below
* [SDK 2.0](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)
for Tello EDU, see the errata below
* [Tello EDU Mission Pad Guide (SDK 2.0)](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20Mission%20Pad%20User%20Guide.pdf)
for Tello EDU
* [Tello Pilots Developer Forum](https://tellopilots.com/forums/tello-development.8/)
is a good developer community
* [Recognizing and Tracking Person of Interest: A Real-Time Efficient Deep Learning based Method for Quadcopters](https://tellopilots.com/forums/tello-development.8/)
