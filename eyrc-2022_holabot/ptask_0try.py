#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (KB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			HB_3347
# Author List:		Ajay Kumar Sahu, Shashwat Srivastava, Adiljith Babu, Kunal Sagar Prasad Singh
# Filename:			task_0.py
# Functions:		update_pose, setInitPose, euclidean_distance, stering, move
# Nodes:		    Add your publishing and subscribing node



####################### IMPORT MODULES #######################
# from mimetypes import init
import sys
import traceback
# from turtle import pu
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
# from math import pow, atan2, sqrt
from math import *
##############################################################



class TurtleBot:
	def __init__(self):
		rospy.init_node('turtlebot_controller', anonymous=True)
		self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)

		self.pose = Pose()
		self.rate = rospy.Rate(60)

		self.init_pose = Pose()
		self.setInitPose()
	
	def update_pose(self, data):
			"""Callback function which is called when a new message of type Pose is
			received by the subscriber."""
			self.pose = data
			self.pose.x = self.pose.x
			self.pose.y = self.pose.y
			self.pose.theta = self.pose.theta
	
	def setInitPose(self):
		""" set the initial postion of turlte """
		vel = Twist()
		# for r in range(2):
		self.velocity_publisher.publish(vel)
		self.rate.sleep()
		self.init_pose.x = self.pose.x
		self.init_pose.y = self.pose.y
		self.init_pose.theta = self.pose.theta
		if self.init_pose.x == 0 or self.init_pose.y ==0:
			self.setInitPose()




	def euclidean_distance(self, goal_pose):
		"""Euclidean distance between current pose and the starting pos."""
		return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))

	def stering(self, goal_pose):
		return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

	def ArcLength(self):
		# b = (self.init_pose.x-self.pose.)
		# a = 90 - tan()
		# return asin(a)/2
		pass

	def move(self):
		vel_msg = Twist()
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0

		# Angular velocity in the z-axis.
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0

		v = 0.5

		stages = [0,0,0]
		while not rospy.is_shutdown():		
			# print(self.pose.theta)
			if stages[0] == 0:
				if self.pose.theta >=0 and self.pose.theta <= pi :
					vel_msg.linear.x = v
					vel_msg.angular.z = v
					# vel_msg.linear.y = 0
				else:
					vel_msg.linear.x = 0
					vel_msg.angular.z = v
					stages[0] = 1
					# vel_msg.linear.y = 0
			
			elif stages[1] == 0:
				if self.pose.theta >= -pi/2 and self.pose.theta < 0 and self.pose.theta < 0:
					vel_msg.angular.z = 0
					vel_msg.linear.x = v
					stages[1] = 1

			elif stages[2] == 0:
				if self.pose.y > self.init_pose.y:
					vel_msg.linear.x = v
				else:
					vel_msg.linear.x = 0
					stages[2] == 1
				# print(self.init_pose.y, self.pose.y)
				# dis = self.euclidean_distance(self.init_pose)
				# if dis


			self.velocity_publisher.publish(vel_msg)
			self.rate.sleep()

	# def stopR(self):


def main():
	x = TurtleBot()
	x.move()


if __name__ == "__main__":
	try:
		print("------------------------------------------")
		print("         Python Script Started!!          ")
		print("------------------------------------------")
		main()

	except:
		print("------------------------------------------")
		traceback.print_exc(file=sys.stdout)
		print("------------------------------------------")
		sys.exit()

	finally:
		print("------------------------------------------")
		print("    Python Script Executed Successfully   ")
		print("------------------------------------------")