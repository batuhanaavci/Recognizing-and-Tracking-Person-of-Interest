# Recognizing and Tracking Person of Interest: 
MathWorks Excellence in Innovation Project 214 Solution

A Real-Time Efficient Deep Learning based Method for Quadcopters

Welcome to the GitHub repository for our project, which extends the work presented in our conference paper titled "Recognizing and Tracking Person of Interest: A Real-Time Efficient Deep Learning based Method for Quadcopters." This repository serves as a comprehensive resource for anyone interested in exploring our project and contributing to its development.

## Project Overview
In this project, we aim to address the challenge of recognizing and tracking a person of interest using quadcopters. Our goal is to develop a real-time, efficient deep learning-based method that enables quadcopters to autonomously detect and track individuals in various scenarios. By leveraging the power of MATLAB and Simulink, we strive to provide a solution with industry relevance and societal impact.

## Key Features and Objectives
- **Real-time Person Recognition**: We employ advanced deep learning techniques to accurately identify individuals in real-time.
- **Efficient Tracking Algorithm**: Our project focuses on developing an efficient tracking algorithm that enables quadcopters to maintain visual contact with the person of interest.
- **Robust Performance**: We aim to create a solution that can handle various environmental conditions, such as changes in lighting, occlusions, and complex backgrounds.
- **Integration with Quadcopter Systems**: Our method is designed to be easily integrated with existing quadcopter systems, facilitating practical implementation and deployment.


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
2. Train your model following the instructions given  in `face_recognition/training/yolov2_train.mlx`
3. Export your new model to file system and move it to the `face_recognition/real-time` folder
4. Edit the `face_recognition/real-time/ros_detect_node.m` file with you new DL models name.
5. Finally run the code.

## Contributions
We appreciate contributions from the community to improve our project. If you would like to contribute, please follow the guidelines outlined in the `contributing.md` file.

## Contact Information
For any questions, suggestions, or feedback, please contact us at:

- Name: [Your Name]
- Email: [Your Email]
- LinkedIn: [Your LinkedIn Profile URL]