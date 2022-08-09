#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from matplotlib.pyplot import gray

import numpy as np 
from keras.models import load_model
import argparse
import imutils

import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())
bridge = CvBridge()

def mean_squared_loss(x1,x2):
  difference=x1-x2
  a,b,c,d,e=difference.shape
  n_samples=a*b*c*d*e
  sq_difference=difference**2
  Sum=sq_difference.sum()
  distance=np.sqrt(Sum)
  mean_distance=distance/n_samples

  return mean_distance

model=load_model("/home/cristiano/catkin_ws/src/vision/scripts/saved_model.h5") #Dar uma olha no path

def talker():
    pub = rospy.Publisher('/webcam',Image,queue_size=1)
    rospy.init_node('image',anonymous=False)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        imagedump=[]
        ret,frame = cap.read()
        if not ret:
            break

        for i in range(10):
            ret,frame=cap.read()
            image = imutils.resize(frame,width=700,height=600)

            frame=cv2.resize(frame, (227,227), interpolation = cv2.INTER_AREA)
            gray=0.2989*frame[:,:,0]+0.5870*frame[:,:,1]+0.1140*frame[:,:,2]
            gray=(gray-gray.mean())/gray.std()
            gray=np.clip(gray,0,1)
            imagedump.append(gray)
        
        imagedump=np.array(imagedump)

        imagedump.resize(227,227,10)
        imagedump=np.expand_dims(imagedump,axis=0)
        imagedump=np.expand_dims(imagedump,axis=4)

        output=model.predict(imagedump)

        loss=mean_squared_loss(imagedump,output)
        print("loss: ",loss)
        if loss > 0.00062:
            print("anomalia")

        msg = bridge.cv2_to_imgmsg(frame,"bgr8")
        pub.publish(msg)
        cv2.imshow('Video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if rospy.is_shutdown():
            cap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInternalException:
        pass