#!/usr/bin/python
# -*- Coding: utf-8 -*-
import serial
import rospy
import copy
from std_msgs.msg import Int64MultiArray
from geometry_msgs.msg import Pose2D

pose_data = Pose2D(x=0,y=0,theta=0)

def pose_CB(data):
    pose_data.x = data.x
    pose_data.y = data.y
    pose_data.theta = data.theta
    # print(str(data.x) + ",x;")
    # print(str(data.y) + ",y;")
    # print(str(data.theta) + ",yaw;")

def main():
    pub = rospy.Publisher('encoder_raw', Int64MultiArray, queue_size=10)
    rospy.Subscriber("/pose2D", Pose2D, pose_CB)
    rospy.init_node('serial_parser_node', anonymous=True)
    with serial.Serial(rospy.get_param("port","/dev/ttyACM0"),rospy.get_param("baudrate",9600),timeout=1) as ser:
        print("port" + rospy.get_param("port",'/dev/ttyACM0'))
        while not rospy.is_shutdown():
            
            send_data = str(pose_data.x) + ",x;" + str(pose_data.y) + ",y;" + str(pose_data.theta) + ",yaw;"

            c = ser.readline()
            datalists = c.split(",")
            datalists_int = Int64MultiArray()
            try:
                for d in datalists: 
                    datalists_int.data.append(int(d))
                print(datalists_int.data)
                pub.publish(datalists_int)
            except ValueError:
                print(d + "Oops!  That was no valid number.")

            ser.write(send_data)
            
        ser.close()
    print("rospy.is_shutdown")
if __name__=="__main__":
    main()
