#!/usr/bin/python
# -*- Coding: utf-8 -*-
import serial
import rospy
from std_msgs.msg import Int64MultiArray

def main():
    pub = rospy.Publisher('encoder_raw', Int64MultiArray, queue_size=10)
    rospy.init_node('serial_parser_node', anonymous=True)
    with serial.Serial(rospy.get_param("port","/dev/ttyACM0"),rospy.get_param("baudrate",9600),timeout=1) as ser:
        print("port" + rospy.get_param("port",'/dev/ttyACM0'))
        while not rospy.is_shutdown():
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

            
        ser.close()
    print("rospy.is_shutdown")
if __name__=="__main__":
    main()
