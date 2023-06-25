#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class HedefeGit():

    def __init__(self):

        rospy.init_node("odom_hiz_node")

        self.hedef_konum = 10.0
        self.guncel_konum = 0.0
        self.kontrol = True
        
        rospy.Subscriber("odom", Odometry, self.odom_hiz_f)

        pub = rospy.Publisher("cmd_vel", Twist, queue_size = 10)
        hiz = Twist()


        rate = rospy.Rate(10)

        while(not rospy.is_shutdown()):

            if(self.kontrol == True):
                
                hiz.linear.x = 1.0
                pub.publish(hiz)

            else:

                hiz.linear.x = 0.0
                pub.publish()
                rospy.loginfo("Hedef konuma ulasildi !")

            rate.sleep()


    def odom_hiz_f(self, mesaj):

        self.guncel_konum = mesaj.pose.pose.position.x

        if(self.guncel_konum < self.hedef_konum):
            
            self.kontrol = True

        else:

            self.kontrol = False     

HedefeGit()

           