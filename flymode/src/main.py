#! /usr/bin/env python3
from sqlite3 import Time
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
inf = math.inf
PI = 3.1415926535897

laserFront = inf 
laserLeft  = inf 
laserRight = inf 
limitDistance = 1.5
speedDrone = 0.5

backtrackingTime = 0

def updateLaserDistance(msg):
    global laserFront
    global laserLeft
    global laserRight

    laserLeft  = msg.ranges[270] 
    laserFront = msg.ranges[540] 
    laserRight = msg.ranges[810] 


class Drone():
    def __init__(self):
        self.subscribe = rospy.Subscriber('/scan',LaserScan,updateLaserDistance)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.rate = rospy.Rate(10) # !!
    
    def direction(self, lin_x=0,lin_y=0,lin_z=0,ang_x=0,ang_y=0,ang_z=0):
        self.control = Twist()
        self.control.linear.x =  lin_x  * speedDrone
        self.control.linear.y =  lin_y  * speedDrone
        self.control.linear.z =  lin_z  * speedDrone

        self.control.angular.x = ang_x 
        self.control.angular.y = ang_y 
        self.control.angular.z = ang_z 
        self.vel_pub.publish(self.control)
        self.rate.sleep()

    def up(self,altitude):
        aux = 0
        while(aux < altitude):
            self.direction(0,0,1,0,0,0)
            aux +=1
        self.stopDrone()

    def stopDrone(self):
        self.direction(0.0,0.0,0.0,0.0)
    
    def moveLeft(self):
        global laserLeft
        print(laserLeft)
        while(laserLeft >= limitDistance):
            print("Sensor Esquerda:",laserLeft)
            self.direction(0,1,0,0,0,0)
        self.stopDrone()
        self.moveBackWithBackTracking()

    def moveRight(self):
        global laserRight
        print(laserRight)
        while(laserRight >= limitDistance):
            print("Sensor Direita:",laserRight)
            self.direction(0,-1,0,0,0,0)
        self.stopDrone()
        self.moveforward()

    def moveforward(self):
        global laserFront
        t0 = rospy.Time.now().to_sec()
        while(laserFront >= limitDistance):
            print("Sensor Frontal:",laserFront)
            self.direction(1,0,0,0,0,0)
        t1 = rospy.Time.now().to_sec()

        global backtrackingTime
        backtrackingTime = t1-t0

        self.moveLeft()

    def moveBack(self):
        self.direction(-1,0,0,0,0,0)

    def moveBackWithBackTracking(self):
        start_time = rospy.Time.now()
        timeout = rospy.Duration(backtrackingTime)

        print('backtracking time..')
        while( (rospy.Time.now() - start_time) < timeout):
            self.moveBack()

        self.stopDrone()
        self.moveRight()

if __name__ == '__main__':
    rospy.init_node('Drone',anonymous=True)
    drone = Drone()
    drone.up(6)
    drone.moveforward()