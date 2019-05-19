cmake_minimum_required(VERSION 2.8.3)
project(localization_comm_to_serial)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
  tf
  tf2
)

## System dependencies are found with CMake's conventions
find_package(Boost REQUIRED COMPONENTS thread system )

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES localization_comm_to_serial
  CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs tf tf2
  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(serial_parser_node src/serial_parser_node.cpp src/serial_parser.cpp)

target_link_libraries(serial_parser_node
  ${catkin_LIBRARIES}
)
