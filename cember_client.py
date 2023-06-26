#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from geometry_msgs.msg import Twist
from ros_python_uygulamalar.srv import Yaricap



def cemberClient():

    rospy.wait_for_service("yaricap_servis")

    try:

        r = float(input("yaricapi giriniz"))
        cember_servis = rospy.ServiceProxy("yaricap_servis", Yaricap)
        cevap = cember_servis(r)

        return cevap.yaricap
    

    except rospy.ServiceException:

        rospy.loginfo("Servis Hatasi !")



cemberClient()


    
    
