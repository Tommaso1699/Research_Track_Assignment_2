# Research_Track_Assignment_2
<h2>About program:</h2>
 Robot is in environment with some obstacles. By sending desired position, robot moves to it. If he finds obstacle, he navigates
 along it to avoid it and then reaches the target position. To do this task, four nodes were developed:
 
  - Node_A_1 implements an action client, allowing the user to set a target (x, y) or to cancel it. In interface we can
    set the desired position of robot, cancel movement or exit process. We navigate via pressing numbers (for example by pressing 
    button '1' we navigate to section where we need to insert desired position on x and y axis). After inserting, we can confirm our 
    choice or go back to main menu.
  
  - Node_A_2 publishes the robot position and velocity as a custom message (x,y, vx, vy), by relying on the values 
    published on the topic /odom.
    
  - Node_B is a service node that, when called, prints the number of goals reached and cancelled
  
  - Node_C subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the 
    target and the robot’s average speed.
    
    
<h2>How to run it:</h2>

 We need to clone 2 repositories to our workspace, where we have ROS installed, in src directory:
 ```
 git clone https://github.com/CarmineD8/assignment_2_2022.git
 git clone https://github.com/Tommaso1699/Research_Track_Assignment_2.git
 ```
 Then we need to download konsole terminal emulator:
 ```
 sudo apt-get update
 sudo apt-get install konsole
 ```
 In our workspace with ROS, we need to run:
 ```
 catkin_make
 source [ws_path]/devel/setup.bash
 ```
 Then in src file we can launch project:
 ```
 roslaunch assignment2_research_track_1 assignment2.launch
 ```
<h2>Pseudocode of Node_A_1:</h2>

```
Initialize Node A_1
Initialize client
Open main menu
Choose number from 1 to 3
If choice is equal to 1:
  Enter position of x coordinate
  Enter position of y coordinate
  Choose if you want to go further or go back to main menu
  If ch is equal to 'y':
    Print x and y
    Wait for server socket
    Initialize goal
    Assign c argument to attribute x
    Assign d argument to attribute y
    Send goal to robot
    Get back to UI
  If ch is equal to 'b':
    Go back to main menu
If choice is equal to 2:
  Choose if you want to go further or go back to main menu
  If ch is equal to 'y':
    Cancel movement of robot
    Go back to main menu
  If ch is equal to 'b':
    Go back to main menu 
```

<h2>Pseudocode of Node_A_2:</h2>


```
Initialize Node A_2
Initialize publisher
Initialize message
Assign value from attribute data.pose.pose.position.x to attribute message.x
Print message.x
Assign value from attribute data.pose.pose.position.y to attribute message.y
Print message.y
Assign value from attribute data.twist.twist.linear.x to attribute message.vx
Print message.vx
Assign value from attribute data.twist.twist.linear.y to attribute message.vy
Print message.vy
Publish message
```

<h2>Possible improvements:</h2>

 - Better algorithm to compute distance from target and average velocity in Node_C
 
 - Computing current position coordinates with more accuracy 
