#!/usr/bin/env python3
#importing libraries
import rospy
from nav_msgs.msg import Odometry
from assignment2_research_track_1.msg import custom_message_position_and_velocity
import time

def Publish(data): #publishing data about coordinates and velocities

    publisher = rospy.Publisher('Position_and_velocity', custom_message_position_and_velocity, queue_size = 10) 

    message = custom_message_position_and_velocity()
    print("\nData: \n")
    message.x = data.pose.pose.position.x
    print("\nPosition on x: ")
    print(message.x)
    message.y = data.pose.pose.position.y
    print("\nPosition on y: ")
    print(message.y)
    message.vx = data.twist.twist.linear.x
    print("\nVelocity on x: ")
    print(message.vx)
    message.vy = data.twist.twist.linear.y
    print("\nVelocity on y: ")
    print(message.vy)
    publisher.publish(message)

# This is main function where there is a subscription to /odom topic, when new message is received, Publish function is invoked 
if __name__ == '__main__': #main
    rospy.init_node('Node_A_2')
    rospy.Subscriber("/odom", Odometry, Publish)
    rospy.spin()

