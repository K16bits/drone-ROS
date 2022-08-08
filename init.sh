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
DIR_HECTOR_MAIN="hector-quadrotor-noetic/hector_quadrotor/hector_quadrotor_demo/launch/"
CONFIG_RVIZ="hector-quadrotor-noetic/hector_quadrotor/hector_quadrotor_demo/rviz_cfg"


# Ambiente Gazebo
cp $BASEDIR/drone-ROS/musthave/square.world $BASEDIR/$DIR_HECTOR_WORLDS
cp $BASEDIR/drone-ROS/musthave/square.launch $BASEDIR/$DIR_HECTOR_LAUNCH

# Configurações RVIZ
cp $BASEDIR/drone-ROS/musthave/rviz_cfg/* $BASEDIR/$CONFIG_RVIZ

# Configurações do Projeto launch
cp $BASEDIR/drone-ROS/musthave/projeto.launch $BASEDIR/$DIR_HECTOR_MAIN

mv $BASEDIR/drone-ROS/flymode/ ./
echo '################### FIM ###########################'