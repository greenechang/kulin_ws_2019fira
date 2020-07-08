#!/usr/bin/env python

import rospy
from op3_utils.op3_utils import Robot
import cv2

robot = Robot('fira_WeightLifting')

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    rospy.init_node('fira_WeightLifting')
    rospy.loginfo(robot.PACKAGE)
    rospy.spin()
