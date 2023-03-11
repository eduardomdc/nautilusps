#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class Publisher:
    def __init__(self):
        rospy.init_node('pub', anonymous=True)
        self.pub = rospy.Publisher('/velocity-sensor', Twist, queue_size=10)
        rospy.Subscriber('/abs-lin-velocity', Float32, self.abs_lin_callback)
        rospy.Subscriber('/abs-ang-velocity', Float32, self.abs_ang_callback)

    def publicar(self):    
        rate = rospy.Rate(5)
        msg = Twist()
        msg.linear.x = 0.44321
        msg.linear.y = -0.593409
        msg.linear.z = 0.9438129
        msg.angular.x = -0.1758
        msg.angular.y = -0.814
        msg.angular.z = 0.17230

        while not rospy.is_shutdown():
            self.pub.publish(msg)
            rate.sleep()

    def abs_lin_callback(self, msg):
        print(f"Linear velocity magnitude: {msg.data}")
    def abs_ang_callback(self,msg):
        print(f"Angular velocity magnitude: {msg.data}")


if __name__ == '__main__':
    publ = Publisher()
    publ.publicar()
