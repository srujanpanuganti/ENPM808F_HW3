# ENPM808F_HW3
Teleoperation and Obstacle avoidance

## Teleoperation 

This program is implemented using ROS in ubuntu 16.04 with Turtlebot installed.
Initialize the roscore by following command
```
roscore
```
type
```
source /opt/ros/kinetic/setup.bash
```
launch the turtlebot world using the below command

```
roslaunch turtlebot_gazebo turtlebot_world.launch
```
using the below command launch the turtlebot teleop world
```
roslaunch turtlebot_teleop keyboard_teleop.launch
```
now use the keys `u i o j k l m ,. `to control the turtlebot from the keyboard.

use the below command to check the Laser sensor data being published
```
rostopic echo /scan
```
screenshots of teleoperation and laserscan messages are attached as `teleop.png` and `laserScan.png` respectively 

## Obstacle Avoidance
first create a catkin workspace as below
```
mkdir catkin_ws
cd catkin_ws
mkdir src
cd src
```
create a package called robot
```
catkin_create_pkg robot
```
create a directory called scripts in the package directory. Here we will place all our scripts 
```
mkdir scripts
```
place the script avoid2.py in this scipts directory and use the below commands to make the avoid2.py as an executable
```
chmod +x avoid2.py
```
now change to your catkin_ws directory and use the commands as below to build your package
```
cd..
cd catkin_ws
catkin_make
source devel/setup.bash
```
Now run the script using the following command
```
rosrun robot avoid2.py
```
Now open a new terminal and give th efollowing command to launch the turtlebot world 
```
roslaunch turtlebot_gazebo turtlebot_world.launch
```
You can see the turtlebot moving by avoiding the obstacles

screenshot of obstacle avoidance is attached as `obstacleAvoidance.png`
The log file for the abstacle avoidance is also added as `state.log` to the repository
