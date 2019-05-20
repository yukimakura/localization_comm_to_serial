# localization_comm_to_serial
|develop|
|---|
|[![Build Status](https://travis-ci.org/yukimakura/localization_comm_to_serial.svg?branch=develop)](https://travis-ci.org/yukimakura/localization_comm_to_serial)|
## Description
laser_scan_matcherから推定された姿勢および自己位置をシリアル通信経由で出力するパッケージです。   
姿勢および自己位置のデータフォーマットは
```
{浮動小数点数のx座標[m]},x;{浮動小数点数のx座標[m]},y;{浮動小数点数のyaw姿勢[rad]},yaw;

[example]
-0.115142214,x;0.5475155521,y;0.84252156212,yaw;
```
となっています。

今後の方針として、scan_matcherにオドメトリーも与えて推定できるように実装していく予定です。

## Requirement
ROS(Kinetic KAME)   
もしくは互換性があるとされる物。

### Subscribe topics   
  sensor_msgs/LaserScan /scan   
### Transforms
  #### Required tf Transforms   
    base_link → laser
       
  #### Provided tf Transforms   
    world → base_link   
       
## Install
```
$ mkdir catkin_ws/src -p
$ cd catkin_ws/src
$ catkin_init_workspace
$ git clone https://github.com/yukimakura/localization_comm_to_serial.git
$ cd ../
$ rosdep install --from-paths src --ignore-src -r -y
$ catkin_make
$ source ~/catkin_ws/devel/setup.bash
```
## Run
`$ roslaunch localization_comm_to_serial localization.launch`   
※USBデバイスのパーミッションが読み書き可能か確認してから実行してください。
## Licence
MIT

## Author

[yukimakura](https://twitter.com/yukimakura86)
