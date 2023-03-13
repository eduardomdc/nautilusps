#!/usr/bin/python3

import rospy
import tf
import math
from tf.transformations import quaternion_from_euler

def sendBodyTransform(body):
	t =  2 * math.pi * (rospy.Time.now().to_sec() / body["orbit-period"]) #parametric variable
	br.sendTransform(
		(body["orbit-radius"]*math.sin(t), body["orbit-radius"]*math.cos(t),0), #parametric equation of a circle
		(0,0,0,1),
		rospy.Time.now(),
		body["name"],
		body["parent"],
	)
	if "moons" in body:
		for moon in body["moons"].values():
			sendBodyTransform(moon) #recursion for moons
	rate.sleep()

if __name__=='__main__':
	rospy.init_node('solar_tf_broadcaster')
	br = tf.TransformBroadcaster()
	rate = rospy.Rate(300.0)
	solar = rospy.get_param("solar")
	while not rospy.is_shutdown():
		for body in solar.values():
			if "orbit-radius" in body:
				sendBodyTransform(body)
			else:
				br.sendTransform(
					(0,0,0), #parametric equation of a circle
					(0,0,0,1),
					rospy.Time.now(),
					body["name"],
					body["parent"],
				)
				rate.sleep()