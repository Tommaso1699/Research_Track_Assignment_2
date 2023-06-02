##
#@package assignment_2_research_track_1
# \file Node_A_1_comment.py
# \brief This file contains code that implements an action client, allowing the user to set a target (x, y) or to cancel it.
# In interface we can set the desired position of robot, cancel movement or exit process. We navigate via pressing numbers 
#(for example by pressing button '1' we navigate to section where we need to insert desired position on x and y axis). After 
#inserting, we can confirm our choice or go back to main menu.
# \author Tomasz Strzesak

#!/usr/bin/env python3
#importing libraries
import rospy
from geometry_msgs.msg import PoseStamped
import actionlib.msg
import assignment_2_2022.msg
import actionlib
import signal
import sys
##
# \brief This function sends coordinates to robot
# \param c is coordinate on x axis
# \param d is coordinate on y axis
# \return This function is type void
def Position(c, d): #sending coordinates to robot
    client.wait_for_server()
##
# goal is type PoseStamped and takes coordinates from c and d parameters
    goal = PoseStamped()
    goal.pose.position.x = c
    goal.pose.position.y = d
    goal = assignment_2_2022.msg.PlanningGoal(goal)
    client.send_goal(goal)
    UI()
##
# \brief This function takes desired coordinates from user
# \return Function returns variables a and b
def coordinates(): #taking desired coordinates from user
    print("Enter x position: ")
##
#  a is taking from user desired position on x axis
    a = int(input())
    print("\nEnter y position: ")
##
#  b is taking from user desired position on y axis
    b = int(input())
    return a, b
##
# \brief This function allows to choose between sending coordinates to robot, cancel movement of robot or exiting process
# \param choice is taking from user number equivalent to desired operation
# \return Function is type void
def switch(choice): #choosing between sending coordinates to robot, cancel movement of robot or exiting process
    if choice == "1": #if user picks number 1
        x,y = coordinates() #coordinates are assigned to x and y variables
        print("Are you sure you want to procede? Type y to continue or b to go back to main menu:\n")
##
#  ch is taking desired operation from user
        ch = input()
        if ch =="b": #going back to main menu
            UI()
        elif ch=="y": #sending coordinates to robot
            print("\nx: " + str(x) + "\ny: " + str(y))
            Position(x,y)
        else:
            print("Wrong input!")
    elif choice == "2": #if user picks number 2
        print("Are you sure you want to procede? Type y to continue or b to go back to main menu:\n")
        ch = input()
        if ch =="b": #going back to main menu
            UI()
        elif ch=="y": #cancel movement of robot
            Cancel()
        else:
            print("Wrong input!")
    else:
        print("Wrong input!")
##
# \brief This function cancels movement of robot
# \return Function is type void
def Cancel(): #cancelling movement of robot
    client.cancel_goal()
    print("Destination is canceled, robot stopped")
    UI()
##
# \brief This function is a signal handler
def handler(signum, frame): #signal handler
    exit(1)
##
# \brief This function is showing a main menu
# \return This function is type void
def UI(): #main menu
    print("\nMenu: \n")
    print("Select destination: press 1\n")
    print("Cancel movement: press 2\n")
##
# choice is taking desired operation from user
    choice = input()  
    signal.signal(signal.SIGINT, handler)
    switch(choice)

if __name__ == '__main__': #main
    rospy.init_node('Node_A_1')
##
# \brief client implements action client
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    UI()
    rospy.spin()

