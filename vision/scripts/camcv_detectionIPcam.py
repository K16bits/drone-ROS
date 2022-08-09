#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from matplotlib.pyplot import gray

import cv2,time

videoCap = cv2.VideoCapture(0)
urlVideo = "http://192.168.50.62:8080/video" # IP fornecido pelo apk IP WebCam

print(videoCap.isOpened())

videoCap.open(urlVideo)

videoCap.set(3,640)
videoCap.set(4,480)
bridge = CvBridge()

xml_haar_cascade = cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml'
faceClassifier =  cv2.CascadeClassifier(xml_haar_cascade)

def talker():
    pub = rospy.Publisher('/webcam',Image,queue_size=1)
    rospy.init_node('image',anonymous=False)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        ret,frame = videoCap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceClassifier.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
        
        cv2.imshow('video',frame)

        msg = bridge.cv2_to_imgmsg(frame,"bgr8")
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if rospy.is_shutdown():
            videoCap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInternalException:
        pass

