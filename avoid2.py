#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
	
	global move 
	if msg.ranges[0] > 0.5:
		move.linear.x = 0.5
		move.angular.z = 0.0

	else:
		move.linear.x = 0.0
		move.angular.z = 0.5
	pub.publish(move)



rospy.init_node('listener',anonymous = True)

pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size = 10)

sub = rospy.Subscriber('/scan', LaserScan, callback)

move = Twist()
				
rospy.spin()

