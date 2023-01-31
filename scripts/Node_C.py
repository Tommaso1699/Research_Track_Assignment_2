#!/usr/bin/env python3
#importing libraries
import math
from assignment_2_2022.msg import custom_message_position_and_velocity
import rospy
#global variables
distance_to_target = 0
average_velocity = 0
i = 0
v = 0
def Position_and_velocity(data): #couting distance to target and average velocity
    global distance_to_target
    global v
    global average_velocity
    global i
    x1 = rospy.get_param("/des_pos_x")
    y1 = rospy.get_param("/des_pos_y")
    x2 = data.x
    y2 = data.y
    distance_to_target= math.sqrt(((x1 - x2)**2)+((y1 - y2)**2))
    vx = data.vx
    vy = data.vy
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
if __name__ == "__main__": #main
    rospy.init_node('Node_C')
    rate = rospy.Rate(rospy.get_param("/frequency"))
    rospy.Subscriber("Position_and_velocity", custom_message_position_and_velocity, Position_and_velocity)
    rate.sleep() #frequency of publishing information
    rospy.spin()
    	
     	
        
