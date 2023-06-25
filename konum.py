#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Konum():

    def __init__(self):

        rospy.init_node("hareket_node")
        rospy.Subscriber("odom", Odometry, self.odom_cb)
        rospy.spin()

    def odom_cb(self, mesaj):

        print(mesaj.pose.pose.position.x)

Konum()


        
