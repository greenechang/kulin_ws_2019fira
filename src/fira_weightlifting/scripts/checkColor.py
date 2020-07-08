#!/usr/bin/env python

import rospy
import cv2
import sys
import numpy as np

def changeHSV(x):
    minH = cv2.getTrackbarPos('minH','Find Color')
    maxH = cv2.getTrackbarPos('maxH','Find Color')
    minS = cv2.getTrackbarPos('minS','Find Color')
    maxS = cv2.getTrackbarPos('maxS','Find Color')
    minV = cv2.getTrackbarPos('minV','Find Color')
    maxV = cv2.getTrackbarPos('maxV','Find Color')
    
    lower = np.array([minH,minS,minV])
    upper = np.array([maxH,maxS,maxV])
  
    #print('lower: ',lower,'upper: ',upper)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    
    #mask = cv2.bitwise_and(hsv, hsv, mask = mask)
    cv2.imshow('Find Color',mask)
    '''
    Right,Yellow:
       ('lower: ', array([20,  0, 71]), 'upper: ', array([ 45, 255, 255]))

    Left,Red:
        ('lower: ', array([152,  99,   0]), 'upper: ', array([179, 255, 255]))

    ''' 
cap = cv2.VideoCapture(0)

# create trackbars for color change
cv2.namedWindow('Find Color', cv2.WINDOW_NORMAL)
cv2.createTrackbar('minH','Find Color', 0,179,changeHSV)
cv2.createTrackbar('maxH','Find Color', 0,179,changeHSV)
cv2.createTrackbar('minS','Find Color', 0,255,changeHSV)
cv2.createTrackbar('maxS','Find Color', 0,255,changeHSV)
cv2.createTrackbar('minV','Find Color', 0,255,changeHSV)
cv2.createTrackbar('maxV','Find Color', 0,255,changeHSV)

  
while not rospy.is_shutdown():
    ret, frame = cap.read()

    
    
    cv2.waitKey(33)
    
