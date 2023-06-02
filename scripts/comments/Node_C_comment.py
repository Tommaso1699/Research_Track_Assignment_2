##
#@package assignment_2_research_track_1
# \file Node_C_comment.py
# \brief This file contains code that subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the target and the robot’s average speed.
# \author Tomasz Strzesak

#!/usr/bin/env python3
#importing libraries
import math
from assignment_2_2022.msg import custom_message_position_and_velocity
import rospy
#global variables
##
# distance_to_target contains distance to goal calculated via mathematical equations
distance_to_target = 0
##
# average_velocity is average velocity during all movement of robot
average_velocity = 0
##
# i  is iterator
i = 0
##
# v is current velocity
v = 0
##
# \brief This function is couting distance to target and average velocity
def Position_and_velocity(data): #couting distance to target and average velocity
    global distance_to_target
    global v
    global average_velocity
    global i
##
# x1 contains coordinate on x axis of desired position  
    x1 = rospy.get_param("/des_pos_x")
##
# y1 contains coordinate on y axis of desired position
    y1 = rospy.get_param("/des_pos_y")
##
# x2 contains current coordinate on x axis
    x2 = data.x
##
# y2 contains current coordinate on y axis
    y2 = data.y
    distance_to_target= math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
##
# vx is current velocity on x axis
    vx = data.vx
##
# vy is current velocity on y axis
    vy = data.vy
##
# velocity is current average velocity of robot 
    velocity= math.sqrt(((vx)**2)+((vy)**2))

    v=v+velocity

    i+=1

    average_velocity=v/i
    if(distance_to_target < 0.5):
        v = 0
        i = 0
        average_velocity = 0
    print("\nDistance to target: " + str(distance_to_target))
    print("\nAverage velocity: " + str(average_velocity))
    
#This is main function where there is a subscription to Position_and_velocity topic, when new message is received, Position_and_velocity function is invoked
#also frequency of published information is set
if __name__ == "__main__": #main
    rospy.init_node('Node_C')
##
# rate is frequency of published information 
    rate = rospy.Rate(rospy.get_param("/frequency"))
    rospy.Subscriber("Position_and_velocity", custom_message_position_and_velocity, Position_and_velocity)
    rate.sleep() #frequency of publishing information
    rospy.spin()
    	
     	
        
