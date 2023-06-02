#!/usr/bin/env python3
#importing libraries
import rospy
from geometry_msgs.msg import PoseStamped
import actionlib.msg
import assignment_2_2022.msg
import actionlib
import signal
import sys

def Position(c, d): #sending coordinates to robot
    client.wait_for_server()

    goal = PoseStamped()
    goal.pose.position.x = c
    goal.pose.position.y = d
    goal = assignment_2_2022.msg.PlanningGoal(goal)
    client.send_goal(goal)
    UI()

def coordinates(): #taking desired coordinates from user
    print("Enter x position: ")

    a = int(input())
    print("\nEnter y position: ")

    b = int(input())
    return a, b

def switch(choice): #choosing between sending coordinates to robot, cancel movement of robot or exiting process
    if choice == "1": #if user picks number 1
        x,y = coordinates() #coordinates are assigned to x and y variables
        print("Are you sure you want to procede? Type y to continue or b to go back to main menu:\n")

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

def Cancel(): #cancelling movement of robot
    client.cancel_goal()
    print("Destination is canceled, robot stopped")
    UI()

def handler(signum, frame): #signal handler
    exit(1)

def UI(): #main menu
    print("\nMenu: \n")
    print("Select destination: press 1\n")
    print("Cancel movement: press 2\n")

    choice = input()  
    signal.signal(signal.SIGINT, handler)
    switch(choice)

if __name__ == '__main__': #main
    rospy.init_node('Node_A_1')

    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    UI()
    rospy.spin()

