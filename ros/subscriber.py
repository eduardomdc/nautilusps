#!/usr/bin/python3

import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

import math



class Subscriber:

    def __init__(self):
        rospy.init_node('sub', anonymous=True)
        rospy.Subscriber('/velocity-sensor', Twist, self.callback)
        self.lin_pub = rospy.Publisher('/abs-lin-velocity', Float32, queue_size = 10)
        self.ang_pub = rospy.Publisher('/abs-ang-velocity', Float32, queue_size = 10)
   
    def callback(self, msg):
        linear = msg.linear
        angular = msg.angular
        abs_lin = math.sqrt(linear.x*linear.x+linear.y*linear.y+linear.z*linear.z)
        abs_ang = math.sqrt(angular.x*angular.x+angular.y*angular.y+angular.z*angular.z)
        reply = Float32()
        reply = abs_lin
        self.lin_pub.publish(reply)
        reply = abs_ang
        self.ang_pub.publish(reply)

if __name__ == '__main__':
    sub = Subscriber()
    rospy.spin()