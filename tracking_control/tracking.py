from tkinter.messagebox import NO
import rclpy
from rclpy.node import Node
import cv2
import math  
from cv_bridge import CvBridge
import time
import json
from sensor_msgs.msg import Image

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Float32
import random
 
from sensor_msgs.msg import Joy

import matplotlib.pyplot as plt
import matplotlib.animation as animation
bridge = CvBridge()

import numpy as np
class PidController:
    def __init__(self):
        self.Kpy = 0.5
        self.Kdy = 0.3
        self.Kpz = 0.4
        self.Kdz = 0.5
        self.Kpx = 0.6
        self.Kdx = 0.4
        self.normalized = []
        self.refy = 0
        self.refz = 0
        self.refx = 0
        self.Az = 0
        self.Ay = 0
        self.Ax = 0
        self.last_errz = 0
        self.last_erry = 0
        self.last_errx = 0
        self.last_posy = 0
        self.last_posz = 0
        self.last_posx = 0
        self.dt = 1
        self.imgWidth = 960
        self.imgHeight = 720
        self.imgWidthCenter = self.imgWidth/2
        self.imgHeightCenter = self.imgHeight/2

    def preprocess(self, box):
        z = (box[1] - self.imgHeightCenter)/self.imgHeightCenter
        y = (box[0] - self.imgWidthCenter)/self.imgWidthCenter
        min_value = 25  # this is the minimum value of the distance, i.e. distance measured when the face is furthest away from drone.
        x = ((box[2]+min_value) - 25)/25

        return z,y,x #normalized error

    def controller(self, target):
        targetz,targety,targetx= self.preprocess(target)
        errz = targetz - self.refz
        erry = targety - self.refy
        errx = targetx - self.refx
        
        self.Az += self.dt* (errz+self.last_errz)/2
        Pz = errz * self.Kpz
        Dz = self.Kdz*(errz - self.last_errz) / self.dt
        uz = Pz + Dz
        self.last_errz = errz

        self.Ay += self.dt* (erry+self.last_erry)/2
        Py = erry * self.Kpy
        Dy = self.Kdy*(erry - self.last_erry) / self.dt
        uy = Py + Dy
        self.last_erry = erry

        self.Ax += self.dt* (errx+self.last_errx)/2
        Px = errx * self.Kpx
        Dx = self.Kdx*(errx - self.last_errx) / self.dt
        ux = Px + Dx
        self.last_errx = errx

        return uz,uy,ux #controller output

    def face_velocity(self,target): 
        dt = 1 
        targety,targetz,targetx= target
        
        self.dY = (targety - self.last_posy) / dt
        self.last_posy = targety

        self.dZ = (targetz - self.last_posz) / dt
        self.last_posz = targetz

        return self.dY, self.dZ


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.listener_callback,
            10)
        
        self.faces_sub = self.create_subscription(
            String,
            'faces',
            self.faces_callback,
            10)
        self.joy_sub = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        
        self.joy_sub  # prevent unused variable warning
        self.faces_sub
        self.faces_data = {}
        self.faces = {}
        self.faces_new = {}

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.error_angular_z_publisher = self.create_publisher(Float32, 'error_angular_z', 10)
        self.error_linear_z_publisher = self.create_publisher(Float32, 'error_linear_z', 10)
        self.error_linear_x_publisher = self.create_publisher(Float32, 'error_linear_x', 10)

        self.subscription  # prevent unused variable warning
        self.publisher_
        self.error_angular_z_publisher 
        self.error_linear_z_publisher 
        self.error_linear_x_publisher 

        self.twist = Twist()
        self.error_angular_z = Float32()
        self.error_linear_z = Float32()
        self.error_linear_x = Float32()


        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timmer_callback)
        self.pid_button = 1
        self.auto = 0
        self.PidController = PidController()

        self.imgWidth = 960
        self.imgHeight = 720
        self.imgWidthCenter = self.imgWidth/2
        self.imgHeightCenter = self.imgHeight/2

        self.center_box = np.array([self.imgHeightCenter, self.imgWidthCenter])  # center coordinates of the reference box (y,z)
        self.rbox_y = self.center_box[0]
        self.rbox_z = self.center_box[1]
        self.Vy = 1
        self.Vz = 1
        self._Kref = 50
        self.enes = 0
        self.batu = 0
        self.omer = 0
        self.berkant = 0
        self.face_to_follow = None

    def faces_callback(self, msg):
        faces_data = json.loads(msg.data)
        if type(faces_data['labels']) == str:
            self.faces = {}
            self.faces[faces_data['labels']] = {'box':faces_data['boxes'] , 'score':faces_data['scores']}

        elif type(faces_data['labels']) == list:
            if len(faces_data['labels']) == 0:
                self.faces = {}
            else:
                                    
                self.faces = {}

                for label in faces_data['labels']:
                    self.faces[label] = {'box':faces_data['boxes'][faces_data['labels'].index(label)] , 'score':faces_data['scores'][faces_data['labels'].index(label)]}
            
    def joy_callback(self, msg):
        self.auto = msg.buttons[5]

        if msg.buttons[0]:
            self.face_to_follow = 'Enes'
        elif msg.buttons[1]:
            self.face_to_follow = 'Batuhan'
        elif msg.buttons[2]:
            self.face_to_follow = 'Yusuf'
        elif msg.buttons[3]:
            self.face_to_follow = 'Muhammed'
    
    def timmer_callback(self):
        if self.auto == 1:
            self.publisher_.publish(self.twist)
            
            self.error_angular_z_publisher.publish(self.error_angular_z)
            self.error_linear_z_publisher.publish(self.error_linear_z)
            self.error_linear_x_publisher.publish(self.error_linear_x)


    def listener_callback(self, msg):
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        cv2.putText(cv_image, 'Face to be Tracked:'+str(self.face_to_follow), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(cv_image, 'Safety Armed'+str(self.auto==1), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        
        
        
        
        if len(self.faces) >0:
            
            for face in self.faces:

                box_y, box_z, box_width, box_height = self.faces[face]['box']
                box_center_y , box_center_z= ((box_y+int(box_width/2)), int((box_z+int(box_height/2))))
                cv2.rectangle(cv_image,(box_y,box_z),(box_y+box_width,box_z+box_height),(0,255,0), thickness=1)  # detected face
                cv2.putText(cv_image, face, (box_y, box_z), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 150, 150), 1, cv2.LINE_AA)

            if self.auto == 1 and self.face_to_follow != None:
                
                if self.face_to_follow in self.faces:
                    print('face detected')
                    box_y, box_z, box_width, box_height = self.faces[self.face_to_follow]['box']
                    box_center_y , box_center_z= ((box_y+int(box_width/2)), int((box_z+int(box_height/2))))
                    
                    cv2.rectangle(cv_image,(box_y,box_z),(box_y+box_width,box_z+box_height),(0,255,0), thickness=1)  # detected face
                    cv2.rectangle(cv_image,(box_center_y-self._Kref,box_center_z-self._Kref),(box_center_y+self._Kref,box_center_z+self._Kref),(255,0,0), thickness=1)  # ref_box
                    cv2.line(cv_image,(box_center_y,box_center_z),(480,360),color=(0, 0, 255), thickness=1)
                    error_y = box_center_y-self.imgWidthCenter
                    error_z = box_center_z-self.imgHeightCenter
                    d = (box_center_y-self._Kref) - box_y
                    error_tuple = (error_y,error_z,d)
                    target = np.array([box_center_y,box_center_z, d])

                    cv2.putText(cv_image, str(error_tuple), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.putText(cv_image, str(face), (10, 175), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                    uz,uy,ux = self.PidController.controller(target)
                    cv2.putText(cv_image, "{:.2f}".format(uz)+"---{:.2f}".format(uy)+"---{:.2f}".format(ux), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 100), 1, cv2.LINE_AA)
                    
                    self.twist.linear.z = -uz
                    self.twist.angular.z = -uy
                    self.twist.linear.x = -ux

                    self.error_angular_z.data = error_y
                    self.error_linear_z.data = error_z
                    self.error_linear_x.data = d

                    
                else:
                    print(str(face),"'s face not detected")
                    
        else:
            cv2.putText(cv_image, 'No Faces Detected', (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow("Detection",cv_image)
        cv2.waitKey(3)


def main(args=None):
    
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':


    main()



