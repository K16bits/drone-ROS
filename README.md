# drone-ROS
Ambiente [ROS Noetic Ninjemys](http://wiki.ros.org/noetic)
```
cd ~/catkin_ws/src
```
Clone este repositorio <br/>
```
git clone https://github.com/K16bits/drone-ROS.git
```
Execute dentro da pasta drone-ROS o .sh
```
./init.sh
```


No diretorio: "~/catkin_ws" execute:
```
source devel/setup.bash
catkin_make
```
## Execução
```
roslaunch hector_quadrotor_demo projeto.launch
```
## Voo 
```
rosrun flymode main.py
```

## Modelos de Visão computacionais 
```
1 - roslaunch vision imshow.launch
2 - roslaunch vision imshowIPCam.launch
3 - roslaunch vision imshow2model.launch 
```
