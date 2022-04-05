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
# Execução
```
roslaunch hector_quadrotor_gazebo testeMain.launch
```
# Mapeamento 
```
rosrun flymode fly3.py
```

![alt map](https://github.com/K16bits/drone-ROS/blob/master/screenshot/mapa.png)
![alt mapaAntes](https://github.com/K16bits/drone-ROS/blob/master/screenshot/antesMapa.png)
![alt mapaDepois](https://github.com/K16bits/drone-ROS/blob/master/screenshot/depoisMapa.png)
