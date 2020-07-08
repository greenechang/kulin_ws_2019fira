#! /usr/bin/python

import rospy
import numpy as np
import cv2

from op3_utils.op3_utils import getWalkingParams, Robot
from op3_utils.vision import *
from copy import copy
import sys

class States:
    INIT = -1
    FIND_BAR = 1
    WALK_2_BAR = 2
    WALK_SIDEWAYS = 3
    PICK_BAR = 4
    WALK_WITH_BAR = 5
    LIFT_BAR = 6
    WALK_2_FINISH = 7
    END = 99

# Functions to be passed to vision system
func1 = detectSingleColor
args1 = ((np.array([13, 120, 80]), np.array([28, 255, 255])),)

# Create vision system
vision = VisionSystem(pipeline_funcs=[func1],
                      pipeline_args=[args1])

# Subscribe to cv_camera topic with vision system
rospy.Subscriber("/cv_camera/image_raw", Image, vision.read, queue_size=1)

# Create robot
robot = Robot()

# Iinitialize Node
rospy.init_node("fira_basketball")

rospy.sleep(3) # Make sure every publisher has registered to their topic,
               # avoiding lost messages

def init():
    # Set ctrl modules of all actions to joint, so we can reset robot position
    robot.setGeneralControlModule("action_module")

    robot.setGrippersPos(left=0.0, right=0.0)

    # Call initial robot position
    robot.playMotion(1, wait_for_end=True)

    # Set ctrl module to walking, this actually only sets the legs
    robot.setGeneralControlModule("walking_module")
    
    # Set joint modules of head joints to none so we can control them directly
    robot.setJointsControlModule(["head_pan", "head_tilt"], ["none", "none"])

    robot.setJointPos(["head_tilt"], [-0.85])

    rospy.sleep(1.0)

def center_head_on_object(obj_pos):
    cx, cy = 0.5, 0.5 # Center of image
    obj_x, obj_y = obj_pos

    dist_x = obj_x - cx
    dist_y = obj_y - cy

    head_curr_x = robot.joint_pos["head_pan"]
    head_curr_y = robot.joint_pos["head_tilt"]

    kp = 0.5
    new_head_x = head_curr_x + kp * -dist_x
    new_head_y = head_curr_y + kp * -dist_y

    robot.setJointPos(["head_tilt", "head_pan"], [new_head_y, new_head_x])

tickrate = 30
rate = rospy.Rate(tickrate)

currState = States.INIT
while not rospy.is_shutdown():
    if currState == States.INIT:
        init()

        # Transition
        tick_count = 0
        currState = States.FIND_BALL

    elif currState == States.FIND_BALL:
        print("[FIND_BALL]")
        # Retrieve results of first function
        status = vision.status[0]
        if status == True:
            tick_count += 1
            center, area = vision.results[0]
            center_head_on_object(center)
        else:
            tick_count = 0

        print(tick_count)

        if tick_count == tickrate:
            # Transition
            tick_count = 0
            robot.walkStart()
            currState = States.WALK

    elif currState == States.WALK:
        print("[WALK]")

        center, area = vision.results[0]
        center_head_on_object(center)
        pan = robot.joint_pos["head_pan"]

        print("Obj X: {}\t Area: {}\t Pan: {}".format(center[0], area, pan))

        if pan > 0.05:
            th = 4.0
        elif pan < -0.05:
            th = -4.0
        else:
            th = 0.0
        robot.walkVelocities(x=8.0, th=th)

        if area > 3100:
            tick_count += 1

            if tick_count == tickrate/2:
                # Transition
                tick_count = 0

                robot.walkStop()

                robot.onlineWalkSetup(x=0.02, foot_dist=0.085, foot_height=0.04)

                currState = States.WALK_SIDEWAYS


    elif currState == States.WALK_SIDEWAYS:
        print("[WALK_SIDEWAYS]")

        center, area = vision.results[0]
        detected = vision.status[0]
        #center_head_on_object(center)
        #rospy.sleep(0.2)
        #pan = robot.joint_pos["head_pan"]
        print("X position of object in image: {} -- Status: {}".format(center[0], detected))

        if center[0] > 0.375:
            robot.onlineWalkCommand(direction="right", start_leg="right", step_num=2,
                side_length=0.02, step_time=0.4)
            rospy.sleep(4)
        else:
            tick_count += 1

            if tick_count == tickrate:
                # Transition
                currState = States.PICK_BALL


    elif currState == States.PICK_BALL:
        print("[PICK_BALL]")
        center, area = vision.results[0]
        center_head_on_object(center)
        pan = robot.joint_pos["head_pan"]
        print(pan)
 
    elif currState == States.END:
        print("[END]")
        robot.walkStop()

        
    rate.sleep()
