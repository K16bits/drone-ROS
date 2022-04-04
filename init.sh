#!/bin/sh
cd ..
BASEDIR="${PWD}"
echo '###############################################'
echo '# Copiando as configurações para o ROS        #'
echo '\n'
git clone https://github.com/RAFALAMAO/hector-quadrotor-noetic.git
sleep 1

DIR_HECTOR_WORLDS="hector-quadrotor-noetic/hector_gazebo/hector_gazebo_worlds/worlds/"
DIR_HECTOR_LAUNCH="hector-quadrotor-noetic/hector_gazebo/hector_gazebo_worlds/launch/"
DIR_HECTOR_MAIN="hector-quadrotor-noetic/hector_quadrotor/hector_quadrotor_gazebo/launch/"
CONFIG_RVIZ="hector-quadrotor-noetic/hector_quadrotor/hector_quadrotor_gazebo/rviz_cfg"
DRONE_MOD="hector-quadrotor-noetic/hector_quadrotor/hector_quadrotor_gazebo/launch/"


git clone "https://github.com/tu-darmstadt-ros-pkg/hector_slam.git"
MAPPING="hector_slam/hector_mapping/launch/"

# Ambiente Gazebo
cp $BASEDIR/drone-ROS/musthave/objects.world $BASEDIR/$DIR_HECTOR_WORLDS
cp $BASEDIR/drone-ROS/musthave/basic.launch $BASEDIR/$DIR_HECTOR_LAUNCH

# Configurações RVIZ
mkdir -p $BASEDIR/$CONFIG_RVIZ
cp $BASEDIR/drone-ROS/musthave/rviz_cfg/* $BASEDIR/$CONFIG_RVIZ

# Configurações DRONE MOD
cp $BASEDIR/drone-ROS/musthave/spawn_quadrotor.launch $BASEDIR/$DRONE_MOD
# Configurações Main launch
cp $BASEDIR/drone-ROS/musthave/testeMain.launch $BASEDIR/$DIR_HECTOR_MAIN

cp $BASEDIR/drone-ROS/musthave/mapping_default.launch $BASEDIR/$MAPPING

git clone https://github.com/ros-teleop/teleop_twist_keyboard.git
mv $BASEDIR/drone-ROS/flymode/ ./
echo '################### FIM ###########################'

# source devel/setup.bash
# roslaunch hector_quadrotor_gazebo testeMain.launch
# rosrun flymode fly3.py