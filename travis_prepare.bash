
#required packages
pip install catkin_pkg --user
pip install empy --user
pip install pyyaml --user
pip install rospkg --user

#ros install
git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu16.04_server.git
cd ./ros_setup_scripts_Ubuntu16.04_server
bash ./step0.bash
bash ./step1.bash

#catkin setup
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
source /opt/ros/kinetic/setup.bash
catkin_init_workspace
cd ~/catkin_ws
catkin_make

#download own package
cd ~/catkin_ws/src/
rsync -av /home/travis/build/*/localization_comm_to_serial ~/catkin_ws/src/
cd ~/catkin_ws/src/localization_comm_to_serial
ls -la
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
catkin_make