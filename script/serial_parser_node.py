#coding utf-8
import serial
from std_msgs.msg import Int64MultiArray

def main():
    pub = rospy.Publisher('encoder_raw', Int64MultiArray, queue_size=10)
    rospy.init_node('serial_parser_node', anonymous=True)
    with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:

        while not rospy.is_shutdown():
            c = ser.readline()
            datalists = c.split(",")
            datalists_int = Int64MultiArray()
            for d in datalists: 
                datalists_int.data.append(int(d))
            print(datalists_int.data)
            pub.publish(datalists_int)
        ser.close()
    print("rospy.is_shutdown")

if __name__=="__main__":
    main()
