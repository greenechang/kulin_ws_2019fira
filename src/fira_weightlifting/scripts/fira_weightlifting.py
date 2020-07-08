#!/usr/bin/env python

import rospy
from op3_utils.op3_utils import *
from vision import *
import cv2
import sys
import rosnode

#Yellow >> Right
#Red >> Left

class States:
    INIT = -1
    GET_READY = 1
    FIND_BAR = 2
    WALK_2_BAR = 3
    WALK_SIDEWAYS = 4
    PICK_BAR = 5
    WALK_WITH_BAR = 6
    LIFT_BAR = 7
    WALK_2_FINISH = 8
    END = 99

# Iinitialize Node
rospy.init_node('fira_weightlifting')


# Create robot ('package_name')
robot = Robot('fira_weightlifting')


while not rospy.is_shutdown():
    if '/op3_manager' in rosnode.get_node_names():
        rospy.loginfo('Found op3 manager')
        break
    else:
        rospy.loginfo('Waiting for op3 manager')
    rospy.Rate(20).sleep()



# Make sure every publisher has registered to their topic,
# avoiding lost messages
rospy.sleep(4) 

DEGREE2RADIAN = np.pi / 180

def init():
    # Set ctrl modules of all actions to joint, so we can reset robot position
    robot.setGeneralControlModule("action_module")
    
    robot.moveGripper(left=100.0,right=100.0)
    #robot.setGrippersPos(left=0.0, right=0.0)
    # >0 is opened
    
    # Call initial robot position
    robot.playMotion(1, wait_for_end=True)

    # Set ctrl module to walking, this actually only sets the legs
    robot.walk_set_param_pub.publish(robot.walking_params[0])
    robot.setGeneralControlModule("walking_module")
    
    # Set joint modules of head joints to none so we can control them directly
    robot.setJointsControlModule(["head_pan", "head_tilt"], ["none", "none"])
    
    
    robot.setJointPos(["head_tilt"], [-0.7])
    #0 is looking straight forward, <0 is looking down

    rospy.sleep(1.0)

tickrate = 30
rate = rospy.Rate(tickrate)

currState = States.INIT

cap = cv2.VideoCapture(0)

current_head_tilt = -0.7
while not rospy.is_shutdown():
    
    
    
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.resize(frame, (0,0),fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    cnts_yellow = findYellowCnts(hsv_frame)
    cnts_red = findRedCnts(hsv_frame)
    delta_head = 0
    delta_lr = 0
    bar_slope = 0
    if (cnts_yellow is not None and cnts_red is not None):
        cx_y, cy_y = findCentroid(cnts_yellow)
        cx_r, cy_r = findCentroid(cnts_red)

        delta_lr = focusCenter(hsv_frame, cx_y, cx_r)
        #print('delta_lr: ' + str(delta_lr))
        delta_head = headTilt(hsv_frame, cy_y, cy_r)
        bar_slope = slope(cx_y, cy_y, cx_r, cy_r)

        cv2.drawContours(hsv_frame, cnts_yellow, -1, (255,0,0), 2)
        cv2.drawContours(hsv_frame, cnts_red, -1, (10,235,290), 2)
        
        cv2.circle(hsv_frame, (int((cx_y + cx_r) / 2),  int((cy_y + cy_r) / 2)),5,(130, 40, 255), -1)
        cv2.circle(hsv_frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)),5,(130, 40, 255), -1)
        
        cv2.circle(hsv_frame, (cx_y, cy_y),5,(130, 40, 255), -1)
        cv2.circle(hsv_frame, (cx_r, cy_r),5,(130, 40, 255), -1)

    #cv2.imshow('Current view',hsv_frame)
    #cv2.waitKey(33)
    
    if currState == States.INIT:
        init()
        currState = States.GET_READY      
        
    elif currState == States.GET_READY:
        print("[GET_READY]")
        if robot.get_pressed_button() == 'start':
            currState = States.FIND_BAR
        #if cv2.waitKey(33) &0xFF == ord('f'):
        #    currState = States.FIND_BAR

    elif currState == States.FIND_BAR:
        print("[FIND_BAR]")
        robot.walking_params.append(robot.loadWalkingParams('param.yaml'))       
        robot.setGeneralControlModule("walking_module")
        robot.walking_params[1].x_move_amplitude = 0.005
        robot.walking_params[1].balance_enable = False
        robot.walking_params[1].y_move_amplitude = 0.003
        #robot.walking_params[1].angle_move_amplitude = 1.75 * DEGREE2RADIAN
        robot.walk_set_param_pub.publish(robot.walking_params[1])
        rospy.sleep(2)
        robot.walkStart()
        currState = States.WALK_2_BAR
        
    elif currState == States.WALK_2_BAR:
        print("[WALK_2_BAR]")
        #if(delta_head < -10):
        
        head_tilt_delta = delta_head * 0.01
        current_head_tilt += head_tilt_delta
        current_head_tilt = max(current_head_tilt,-1.2)
        print('current head: {},  head_tilt_delta: {}'.format(current_head_tilt,head_tilt_delta))
        
        robot.moveHead(None, current_head_tilt)
        print("delta_lr: {}".format(delta_lr))
        ratio = 1
        angle_delta = delta_lr * ratio
        print("*********************************************")
        
        
        robot.walking_params[1].angle_move_amplitude = angle_delta
        robot.walk_set_param_pub.publish(robot.walking_params[1])
        print("angle_move_amp: ", angle_delta)
        '''
        if(delta_lr > 20):
            print("GO LEFT")
            robot.walking_params[1].angle_move_amplitude = angle_delta
            robot.walk_set_param_pub.publish(robot.walking_params[1])
            print("angle_move_amp: ", angle_delta)
        
        elif(delta_lr < -20):
            print("GO RIGHT")
            robot.walking_params[1].angle_move_amplitude = angle_delta
            robot.walk_set_param_pub.publish(robot.walking_params[1])
            print("angle_move_amp: ", angle_delta)
            
        else:
            print("GO FORWARD")
            robot.walking_params[1].angle_move_amplitude = 0
            robot.walk_set_param_pub.publish(robot.walking_params[1])
            print("angle_move_amp: ", angle_delta) 
        '''
        
        
        if(current_head_tilt == -1.2):
          
            robot.walkStop()
            robot.onlineWalkSetup(x=0.02, z=-0.025, foot_dist=0.08, foot_height=0.05)
            currState = States.WALK_SIDEWAYS
            continue
        
    elif currState == States.WALK_SIDEWAYS:
        ret, frame = cap.read()
        print("bar_slope: {}".format(bar_slope))

        bar_x = (cx_y + cx_r) / 2
        bar_y = (cy_y + cy_r) / 2
        print("bar_location: ({},{})".format(bar_x,bar_y))
        x_err = bar_x - hsv_frame.shape[1] / 2
        y_err = bar_y - hsv_frame.shape[0] *2 / 3
        print("bar_error: ({},{})".format(x_err,y_err))
        '''
        if y_err > 20:
            print('back')
            robot.onlineWalkCommand(direction="backward", start_leg="right", step_num=2,
                    front_length=0.02, step_time=0.5)
            rospy.sleep(2)
        '''            
        
        if bar_slope <= -0.07:
            print('turn left')
            robot.onlineWalkCommand(direction="turn_left", start_leg="left", step_num=2,
                    front_length=0.0, step_angle=10.0,step_time=0.4)
            rospy.sleep(2)

        elif bar_slope > 0.07:
            print('turn right')

            robot.onlineWalkCommand(direction="turn_right", start_leg="right", step_num=2,
                    front_length=0.0, step_angle=10.0,step_time=0.4)
            rospy.sleep(2)
            '''    
            elif x_err > 30:
                print('shift right')
                robot.onlineWalkCommand(direction="right", start_leg="right", step_num=2,
                        side_length=0.01, step_time=0.4)
                rospy.sleep(2.5)
                
            elif x_err < -30:
                print('shift left')
                robot.onlineWalkCommand(direction="left", start_leg="left", step_num=2,
                        side_length=0.01, step_time=0.4)
                rospy.sleep(2.5)
                
            elif y_err < -20:
                print('forward')
                robot.onlineWalkCommand(direction="forward", start_leg="right", step_num=2,
                        front_length=0.02, step_time=0.4)
                rospy.sleep(2)
            '''
        else:    
            print('success!!!')
            # TODO removed sleep here
            #rospy.sleep(6)
            currState = States.PICK_BAR
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()
        ret, frame = cap.read()

        
        
        
        '''
        print("[WALK_SIDEWAYS]")
        print("bar_slope: {}".format(bar_slope))
       
        if(bar_slope > 0.1):
            print("Turn facing right")
            robot.walking_params[1].x_move_amplitude = 0
            robot.walking_params[1].y_move_amplitude = -0.01
            robot.walk_set_param_pub.publish(robot.walking_params[1])
            rospy.sleep(2)
            robot.walkStart()
            rospy.sleep(2)
            robot.walkStop()
            
        elif(bar_slope < -0.1):
            print("Turn facing left")
            robot.walking_params[1].x_move_amplitude = 0
            robot.walking_params[1].y_move_amplitude = 0.01
            robot.walk_set_param_pub.publish(robot.walking_params[1])
            rospy.sleep(2)
            robot.walkStart()
            rospy.sleep(2)
            robot.walkStop()
        else:
            print("Keep facing forward")
            
            currState = States.PICK_BAR
        '''
    elif currState == States.PICK_BAR:
        rospy.loginfo("[PICK_BAR]")
        # TODO testing
        #rospy.sleep(2)
        robot.setGeneralControlModule("none")
        rospy.sleep(2)
        robot.setGeneralControlModule("action_module")
        
        robot.playMotion(86, wait_for_end=True)
        robot.playMotion(87, wait_for_end=True)
        rospy.sleep(1.0)
        robot.moveGripper(left=40.0,right=40.0)
        rospy.sleep(0.5)
        robot.moveGripper(left=20.0,right=20.0) 
        rospy.sleep(1.0)
        robot.playMotion(90, wait_for_end=True)
        rospy.sleep(1.0)
        currState = States.WALK_WITH_BAR

    elif currState == States.WALK_WITH_BAR:
        print("[WALK_WITH_BAR]")
        
        
        robot.walking_params.append(robot.loadWalkingParams('pickup_param.yaml'))
        #robot.walking_params[2].hip_pitch_offset = -5
        robot.walking_params[2].x_move_amplitude = 0.005
        robot.walking_params[2].y_move_amplitude = 0.000
        #TODO change the a move amplitude to 1
        robot.walking_params[2].angle_move_amplitude = 0 * DEGREE2RADIAN
        robot.walk_set_param_pub.publish(robot.walking_params[2])
        # Set ctrl module to walking, this actually only sets the legs
        robot.setJointsControlModule(["r_hip_yaw","l_hip_yaw","r_hip_roll","l_hip_roll","r_hip_pitch",
        "l_hip_pitch","r_knee","l_knee","r_ank_pitch","l_ank_pitch","r_ank_roll","l_ank_roll"],
        ["walking_module"])
        print(robot.walking_params[2])
        rospy.sleep(3)
        robot.walkStart()
        rospy.sleep(3)
        robot.moveGripper(left=15.0,right=15.0) 
        rospy.sleep(9)

        robot.walkStop()
        currState = States.LIFT_BAR

    elif currState == States.LIFT_BAR:
        print("[LIFT_BAR]")
        robot.setGeneralControlModule("none")
        robot.setGeneralControlModule("action_module")
        robot.playMotion(89, wait_for_end=True)
        robot.setJointsControlModule(['head_pan', 'head_tilt'],['none','none'])
        robot.moveHead(0,1.5)
        currState = States.WALK_2_FINISH

    elif currState == States.WALK_2_FINISH:
        print("WALK_2_FINISH")
        
        robot.walking_params.append(robot.loadWalkingParams('pickup_param.yaml'))
        robot.walking_params[3].hip_pitch_offset = 1 * DEGREE2RADIAN #1.5
        robot.walking_params[3].x_move_amplitude = 0
        robot.walking_params[3].balance_enable = True
        robot.walk_set_param_pub.publish(robot.walking_params[3])
        
        # Set ctrl module to walking, this actually only sets the legs
        robot.setJointsControlModule(["r_hip_yaw","l_hip_yaw","r_hip_roll","l_hip_roll","r_hip_pitch",
        "l_hip_pitch","r_knee","l_knee","r_ank_pitch","l_ank_pitch","r_ank_roll","l_ank_roll"],
        ["walking_module"])
        rospy.sleep(5)
        robot.walkStart()
        rospy.sleep(3)
        robot.walking_params[3].x_move_amplitude = 0.005
        robot.walk_set_param_pub.publish(robot.walking_params[3])
        rospy.sleep(1117)
        robot.walkStop()
        currState = States.END
        rate.sleep()    
    elif currState == States.END:
        print("[END]")
        #robot.walkStop()

        
    rate.sleep()
