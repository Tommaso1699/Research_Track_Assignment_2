#!/usr/bin/env python3
#importing libraries
import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os
#global variables

reached_goal =0

canceled_goal = 0

def Goals(arg): #printing reached and canceled goals

# reached_goals contains a number of reached goals
# canceled_goals contains a number of canceled goals
    global  reached_goal, canceled_goal 
    print("Reached goals: " + str(reached_goal) + " Canceled goals: " + str(canceled_goal) )
    return EmptyResponse()

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

    
    
    
