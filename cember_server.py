#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from geometry_msgs.msg import Twist
from ros_python_uygulamalar.srv import Yaricap


def yaricapHareket(istek):

    hiz = Twist()

    lineer_hiz = 0.5
    hiz.linear.x = lineer_hiz

    r = istek.yaricap

    # w(acial hiz) = v(hiz) / r(yaricap)


    hiz.angular.z = (hiz.linear.x) / r


    while(not rospy.is_shutdown()):

        pub.publish(hiz)


def cemberServer():

    global pub
    
    rospy.init_node("cember_server_node")
    rospy.Service("yaricap_servis", Yaricap, yaricapHareket)

    pub = rospy.Publisher("cmd_vel", Twist, queue_size = 10)

    rospy.spin()



if __name__ == "__main__":

    cemberServer()
