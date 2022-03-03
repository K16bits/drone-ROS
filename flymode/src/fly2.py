#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

print("---- Run ---")

class Fly():
    def __init__(self):
        self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.rate=rospy.Rate(2)

    def direction(self, lin_x=0,lin_y=0,lin_z=0,ang_x=0,ang_y=0,ang_z=0):
        self.control = Twist()
        self.control.linear.x =  lin_x  
        self.control.linear.y =  lin_y
        self.control.linear.z =  lin_z # up voou

        self.control.angular.x = ang_x
        self.control.angular.y = ang_y
        self.control.angular.z = ang_z
        self.pub.publish(self.control)
        self.rate.sleep()
    
    def up(self,altitude):
        aux = 0
        while(aux < altitude):
                self.direction(0,0,1,0,0,0)
                aux +=1
        self.direction(0,0,0,0,0,0)

    def turn(self):
        aux = 0
        while(aux < 3):
            self.direction(0,0,0,0,0,1)
            aux+=1
        self.direction(0,0,0,0,0,0)

    def moveInline(self,metros):
        aux = 0
        while(aux < metros):
            self.direction(1,0,0,0,0,0)
            aux +=1 
        self.direction(0,0,0,0,0,0)
    
def callback(msg):
    print('360')
    print(msg.ranges[360])
    if(msg.ranges[360] < 1):
        print(msg.ranges[360])



if __name__ == '__main__':
    rospy.init_node('droneMove',anonymous=True)
    drone = Fly()
    rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
    altitude = 5
    metros = 4

    drone.up(altitude)
    drone.moveInline(metros)
    # for i in range(1,5):
    #     drone.moveInline(metros)
    #     drone.turn()

