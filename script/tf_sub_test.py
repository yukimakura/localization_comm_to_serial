#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
 
if __name__ == '__main__':
    rospy.init_node('tf_turtle')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/base_link', '/laser', rospy.Time(0))
            print(trans.value)
            print(rot.value)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("tf err.")
            continue
 
        
        rate.sleep()