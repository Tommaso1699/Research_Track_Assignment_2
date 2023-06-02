##
#@package assignment_2_research_track_1
# \file Node_B_comment.py
# \brief This file contains a service node that, when called, prints the number of goals reached and cancelled
# \author Tomasz Strzesak

#!/usr/bin/env python3
#importing libraries
import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
#global variables
##
# reached_goals contains a number of reached goals, which is incremented if goal is reached
reached_goal =0
##
# canceled_goals contains a number of canceled goals, which is incremented if goal is canceled
canceled_goal = 0
##
# \brief This function is printing reached and canceled goals
# \param arg is a parameter
# \return Function returns EmptyResponse()
def Goals(arg): #printing reached and canceled goals

# reached_goals contains a number of reached goals
# canceled_goals contains a number of canceled goals
    global  reached_goal, canceled_goal 
    print("Reached goals: " + str(reached_goal) + " Canceled goals: " + str(canceled_goal) )
    return EmptyResponse()
##
# \brief This function is counting reached and canceled goals
# \param data contains status of goal
# \return Function is type void
def Counter(data): #counting reached and canceled goals
    if data.status.status == 2:

        global canceled_goal
        canceled_goal += 1
        os.system('rosservice call Goals_reached_and_canceled')
    
    elif data.status.status == 3:

        global reached_goal
        reached_goal += 1
        os.system('rosservice call Goals_reached_and_canceled')

# This is main function where there is a subscription to /reaching_goal/result topic, when new message is received, Counter function is invoked
#also service is provided 
if __name__ == "__main__": #main
    rospy.init_node('Node_B')
    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, Counter)
    rospy.Service('Goals_reached_and_canceled',Empty,Goals)
    rospy.spin()

    
    
    
