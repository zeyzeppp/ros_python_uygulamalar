#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from geometry_msgs.msg import Twist

def tek_eksen_hareket():

    rospy.init_node("tek_hareket_node")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size = 10)

    hiz = Twist()
    hiz.linear.x = 0.5
    alinacak_yol = 5
    alinan_yol = 0

    t0 = rospy.Time.now().to_sec()

    while(alinan_yol < alinacak_yol):

        pub.publish(hiz)
        t = rospy.Time.now().to_sec()
        alinan_yol = (hiz.linear.x) * (t-t0)

    hiz.linear.x = 0.0
    pub.publish(hiz)
    rospy.loginfo("gorev tamamlandi!")


tek_eksen_hareket()
