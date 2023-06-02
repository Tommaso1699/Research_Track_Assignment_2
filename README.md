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
 We need to open terminal and run:
 ```
 roscore&
 ```
 
 In our workspace with ROS, we need to run:
 ```
 catkin_make
 source [ws_path]/devel/setup.bash
 ```
 If necessary, we need to make python files in scripts folder executable. To do that,
 we move to directory scripts in directory Research_Track_Assignment_2 and we run:
  ```
 chmod 777 ./*
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
Choose number from 1 to 2
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

<h2>Documentation:</h2>

 Documentation of all nodes was added using Doxygen. Due to problems with running code
after adding comments suitable for Doxygen, I created new folder in scripts folder named
comments, where I put all python scripts with nodes and comments in doxygen format. We can
generate HTML page by running doxywizard in CLI and choosing appropriate fields:

![Screenshot from 2023-06-02 13-30-11](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/55e1c763-9b18-4b7f-8d0c-2640be460466)

 We can navigate on a page using panel on the left. We can see README and comments folder with commented node scripts:
 
 ![Screenshot from 2023-06-02 13-28-23](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/7c8caa31-a629-45c7-ab76-7e62126cba74)
 
![Screenshot from 2023-06-02 13-28-47](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/f7f20374-0202-4e0f-87d9-1f5126b9484b)

![Screenshot from 2023-06-02 13-29-01](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/f366d157-a4ae-4b50-8366-67054e7f9d33)

![Screenshot from 2023-06-02 13-29-09](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/31dec341-8a00-4057-a137-94b0b0418654)

![Screenshot from 2023-06-02 13-29-15](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/b30aa7a7-8d0c-4b8e-a9f1-a18855959025)

![Screenshot from 2023-06-02 13-29-23](https://github.com/Tommaso1699/Research_Track_Assignment_2/assets/69764736/bc804ff8-568c-4b13-9c61-b98ed596a629)

<h2>Jupyter Notebook:</h2>
 We can run Jupyter notebook as a main menu and navigate a robot. In CLI we need to run command:
 
 ```
 jupyter notebook --allow-root
 ```
 Then when we run notebook, we can select  desired position, check send goal and press confirm action button:
 
 When we want to cancel movement, we uncheck send goal, check cancel and press confirm action button.
 
 At the bottom we can see plots with displaying values of position and distance to closest obstacle:
 
 

