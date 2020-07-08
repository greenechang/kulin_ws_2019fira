#!/usr/bin/env python

import os
import numpy as np
import yaml
import pandas as pd
import time

import rospy
import cv2
from cv2 import aruco
from cv_bridge import CvBridge, CvBridgeError

#import rosparam
import rosnode

from sensor_msgs.msg import Image, JointState
from std_msgs.msg import String, Int32

from robotis_controller_msgs.msg import StatusMsg
from op3_walking_module_msgs.msg import WalkingParam

from robotis_controller_msgs.srv import SetModule, SetJointModule
from op3_action_module_msgs.srv import IsRunning


from op3_ros_function import *
DATA_PATH = '/home/robotis/Kulin_ws/src/sprint/data/'
CONFIG_PATH = '/home/robotis/Kulin_ws/src/sprint/config/'
PACKAGE_PATH = '/home/robotis/Kulin_ws/src/sprint/'

DEGREE2RADIAN = np.pi / 180

MODE_LIST = ['READY',
             'SPRINT',
             'MODE_NUM']


STR_X = 0.007
STR_Y = 0
STR_A = 0 * DEGREE2RADIAN



current_mode = 0
is_start = 0

#Publisher setup
walk_command_pub = rospy.Publisher('/robotis/walking/command', String, queue_size=1)
walk_set_param_pub = rospy.Publisher('/robotis/walking/set_params', WalkingParam, queue_size=5)
action_page_pub = rospy.Publisher('/robotis/action/page_num', Int32, queue_size=5)
base_init_pub = rospy.Publisher('/robotis/base/ini_pose', String, queue_size=5)
set_joint_states_pub = rospy.Publisher('/robotis/set_joint_states',JointState, queue_size=5)

WALKING_STRAIGHT = init_walking_param('param.yaml')



def button_callback(msg):
    '''Callback function when receive a message from rostpoic /robotis/open_cr/button

    To manage modes in obstacle_run by global variables "current_mode" and "is_start"

    Args:
        msg: std_msgs.msg.String
    Returns:
        none

    '''

    global is_start

    rospy.loginfo('button pressed: ' + msg.data)
    if msg.data == 'mode' or msg.data == 'mode_long':
        global current_mode
        is_start = 0
        current_mode += 1
        if current_mode == 2:
            current_mode = 0

        rospy.loginfo('current mode:' + MODE_LIST[current_mode])

    elif msg.data == 'start' or msg.data == 'start_long':
        is_start = 1
        page_num = 1
        action_page_pub.publish(1)
        while action_is_running_client():
            rospy.Rate(1000).sleep()
            rospy.loginfo('waiting other action')
        action_page_pub.publish(15)
        rospy.loginfo('Start mode: ' + MODE_LIST[current_mode])




def status_callback(msg):
    '''Callback finction when receive a message from rostopic /robotis/status
    1. Enable walking module after Init Pose.

    '''
#   rospy.loginfo('Got Status Msg: '+msg.status_msg)

    #Active walking module after initialization
    if msg.status_msg == 'Finish Init Pose':
        module_name = 'walking_module'
        rospy.loginfo('Set ctrl module: ' + module_name +' result:'+ \
str(set_ctrl_module_client(module_name)))
        module_name = 'none'
        rospy.loginfo('Set joint ctrl module: ' + module_name +' result:'+ \
str(set_joint_ctrl_module_client('head_pan', module_name)))
        rospy.loginfo('Set joint ctrl module: ' + module_name +' result:'+ \
str(set_joint_ctrl_module_client('head_tilt', module_name)))
        rospy.Rate(1).sleep()

        move_head(0,-0.15)


#States list
READY            = 0
START_FORWARD    = 1
FORWARD          = 2
STOP_FORWARD     = 3
STOP             = 4
START_BACKWARD   = 5
BACKWARD         = 6

STATE_LIST = ['ready',
              'start_forward',
              'forward',
              'stop_forward',
              'stop',
              'start_backward',
              'backward']

state = 0

frame = cv2.imread("/home/robotis/Kulin_ws/src/sprint/scripts/0.jpg")

BRIDGE = CvBridge()
def camera_callback(msg):
    ''' Callback function when receive a message from rostopic /cv_camera/image_raw

    Use CvBridge to convert image_raw to numpy array.
    Then call frame_process().

    Args:
        msg: sensor_msgs.msg.Image
    Returns:
        none
    '''
    try:
        global frame
        frame = BRIDGE.imgmsg_to_cv2(msg, "bgr8")
        #frame = cv2.resize(cv2_img, (0, 0), fx=1, fy=1)
    except CvBridgeError, err:
        rospy.loginfo(err)
    '''
    else:
        frame_process(frame)
    '''



#def frame_process(frame):
    '''Main process
    
    '''
    '''Main image processing area.

    Args:
        frame: A numpy array, image catched from webcam.
    '''
markerLength = 20

def read_mtx_dist_yaml():
    with open('/home/robotis/Kulin_ws/Other Codes/calibration.yaml') as f:
        loadeddict = yaml.load(f)
    mtx = loadeddict.get('camera_matrix')
    dist = loadeddict.get('dist_coeff')
    mtx = np.array(mtx)
    dist = np.array(dist)
    return mtx, dist


aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters =  aruco.DetectorParameters_create()

parameters.adaptiveThreshWinSizeMin = 13 #default=3
parameters.adaptiveThreshWinSizeMax = 23 #default=23
parameters.adaptiveThreshWinSizeStep = 5 #default=10
parameters.perspectiveRemovePixelPerCell = 12 #default=8
parameters.minMarkerPerimeterRate = 0.06 #default=0.03
    
#parameters.perspectiveRemoveIgnoredMarginPerCell =0.16 #default=0.13
#parameters.maxErroneousBitsInBorderRate = 0.4 #default=0.35


def detect_Aruco(img):
    aruco_list = {}
    mtx, dist = read_mtx_dist_yaml()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h,  w = gray.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
    
    
    #rospy.loginfo('adaptThreshWinSizeMStep :' + str(parameters.adaptiveThreshWinSizeStep))
    #rospy.loginfo('adaptThreshWinSizeMin :' + str(parameters.adaptiveThreshWinSizeMin))
    #rospy.loginfo('adaptThreshWinSizeMax :' + str(parameters.adaptiveThreshWinSizeMax))
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters = parameters)
    #print("ids: ",ids)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if np.all(ids == 33):
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, mtx, dist) # For a single marker
        imgWithAruco = aruco.drawDetectedMarkers(img, corners, ids, (0,255,0))
        imgWithAruco = aruco.drawAxis(imgWithAruco, mtx, dist, rvec, tvec, 40)
        #print("rvec: ",rvec)
        #print("tvec: ",tvec)
        #rospy.loginfo("rvec: "+ str(rvec))
        #rospy.loginfo("tvec: "+ str(tvec))
        if len(corners):  # returns no of arucos
            for k in range(len(corners)):
                temp_1 = corners[k]
                temp_1 = temp_1[0]
                temp_2 = ids[k]
                temp_2 = temp_2[0]
                
                aruco_list[temp_2] = temp_1
            #print('Aruco List:',aruco_list)
            rospy.loginfo("Aruco list: "+ str(aruco_list))
        #print("------------------------------------")
    else:   # if aruco marker is NOT detected
        imgWithAruco = img  # assign imRemapped_color to imgWithAruco directly
        return None, None, None, None
    #cv2.imshow("aruco", imgWithAruco)   # display
    #cv2.putText(img, "Id: " + str(ids), (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)
    return ids, rvec, tvec, aruco_list

def locateByAruco(img, ids, rvec, tvec):
    if np.all(ids == 33):
        y_offset = rvec[0][0][2]
        distance = tvec[0][0][2]
        #print("y_offset: ", y_offset)
        rospy.loginfo("distance: "+str( distance))
        rospy.loginfo("y_offset: "+str(y_offset))
    else:   # if aruco marker is NOT detected
        return None, None
    return y_offset, distance

def markCenter(img, aruco_list):

    if aruco_list == None:
        #rospy.loginfo('aruco == None')
        return    
    key_list = aruco_list.keys()
    #print('Key List:',key_list)
    #font = cv2.FONT_HERSHEY_SIMPLEX    
    for key in key_list:
        dict_entry = aruco_list[key]  # dict_entry is a numpy array with shape (4,2)
        centerOfAruco = dict_entry[0] + dict_entry[1] + dict_entry[2] + dict_entry[3]  # so being numpy array, addition is not list addition
        centerOfAruco[:] = [int(x / 4) for x in centerOfAruco]  # finding the centre
        
        centerOfAruco = tuple(centerOfAruco)
        orient_center = tuple((dict_entry[0] + dict_entry[1]) / 2)
        #print ("centerOfAruco: ",centerOfAruco)
        # print orient_center
        cv2.circle(img, centerOfAruco, 1, (0, 0, 255), 3)
        cv2.circle(img, tuple(dict_entry[0]), 1, (0, 0, 255), 3)
        cv2.circle(img, tuple(dict_entry[1]), 1, (0, 255, 0), 3)    
        cv2.circle(img, tuple(dict_entry[2]), 1, (255, 0, 0), 3)
        cv2.circle(img, orient_center, 1, (0, 0, 255), 3)
        #cv2.line(img, centerOfAruco, orient_center, (255, 0, 0), 4)  # marking the centre of aruco
       # cv2.putText(img, str(key), (int(centre[0] + 20), int(centre[1])), font, 1, (0, 0, 255), 2,cv2.LINE_AA)  # displaying the idno
    return centerOfAruco[0]

def findCenterOfScreen(img):
    y, x= img.shape[0:2]
    #print("x: ",x ,"y: ",y)

    centerOfScreen=(int(x/2),int(y/2)) #Cx, Cy
    #print("centerOfScreen:" ,centerOfScreen)
    cv2.circle(img, centerOfScreen, 10, (255, 255, 255), 3  )
    #cv2.imshow('center', img)
    return centerOfScreen[0]


found = 1.0
not_found = 1.0

if __name__ == '__main__':
    pre_y_offset = 0
    
    rospy.init_node('sprint', disable_signals=True)
    
    rospy.loginfo('Sprint node open.')

    #Subscriber setup
    rospy.Subscriber("/robotis/open_cr/button", String, button_callback)
    rospy.Subscriber("/cv_camera/image_raw", Image, camera_callback)
    rospy.Subscriber("/robotis/status", StatusMsg, status_callback)

    # check if op3_manager is working
    while not rospy.is_shutdown():
        if '/op3_manager' in rosnode.get_node_names():
            rospy.loginfo('Found op3 manager')
            break
        else:
            rospy.loginfo('Waiting for op3 manager')
        rospy.Rate(20).sleep()

        
    global state
    global WALKING_STRAIGHT
    
    head_pan = 0
    

    while not rospy.is_shutdown():
        image = frame
        ids, rvec, tvec, aruco_list = detect_Aruco(frame)
        centerXofAruco = markCenter(frame, aruco_list) 
        y_offset, distance = locateByAruco(frame, ids, rvec, tvec)
        print("DISTANCEEEEEEE: {}".format(distance))    
        centerXOfScreen = findCenterOfScreen(frame)
        # Sprint run mode
        if (distance != None):
            found+=1
        rospy.loginfo('State: ' + STATE_LIST[state])
        if current_mode == 1:
            #rospy.loginfo('Sprint run mode.')
            if (distance != None):

                y_offset = y_offset * 140 /distance
                
                if (y_offset > pre_y_offset) and (y_offset - pre_y_offset >= 0.2):
                    y_offset = pre_y_offset + 0.1
                    
                elif (pre_y_offset > y_offset) and (pre_y_offset - y_offset >= 0.2):
                    y_offset = pre_y_offset - 0.1
                pre_y_offset = y_offset

                #centerXofAruco = markCenter(frame, aruco_list) 
                
                turn = (centerXofAruco-centerXOfScreen)/frame.shape[1]
                rospy.loginfo('distance: '+ str(distance))
                #rospy.loginfo('turn: '+ str(turn))

                if state == FORWARD:
                    WALKING_STRAIGHT.x_move_amplitude = 0.02
                    WALKING_STRAIGHT.angle_move_amplitude = turn * -0.5
                    WALKING_STRAIGHT.balance_enable = True
                    walk_set_param_pub.publish(WALKING_STRAIGHT)
                    walk_command_pub.publish('start')
                    
                    if(distance <= 80):
                        rospy.loginfo("SLOW DOWN, BRO")
                        state = STOP_FORWARD
                        move_head(0,-0.1)
                        
                elif state == BACKWARD:
                    head_pan += turn * -0.3
                    rospy.loginfo('head_pan: {}'.format(head_pan))
                    #move_head(head_pan,-0.2)
                    WALKING_STRAIGHT.x_move_amplitude = -0.02
                    a = y_offset * -0.6 - 0.04


                    #WALKING_STRAIGHT.angle_move_amplitude = head_pan *  0.4
                    # WALKING_STRAIGHT.y_move_amplitude =  y_offset * 0.07 * distance / 180
                    WALKING_STRAIGHT.y_move_amplitude = 0
                    WALKING_STRAIGHT.z_swap_amplitude = -0.000
                    WALKING_STRAIGHT.init_z_offset = 0.05
                   
                    a = min(max(a,-0.1),0.03)
                    WALKING_STRAIGHT.angle_move_amplitude = a
                    if distance >= 200:
                        a = min(max(a,-0.025),0.00)
                        #a = 0
                        WALKING_STRAIGHT.angle_move_amplitude = a
                        WALKING_STRAIGHT.y_move_amplitude = 0.001
                    WALKING_STRAIGHT.balance_enable = True
                    walk_set_param_pub.publish(WALKING_STRAIGHT)
                    walk_command_pub.publish('start')
                    #rospy.sleep(5)
                    
                    #walk_command_pub.publish('stop')
                    #rospy.sleep(1.5)
                        
            if state == READY:
                #rospy.Rate(2).sleep()
                WALKING_STRAIGHT.x_move_amplitude = 0
                WALKING_STRAIGHT.balance_enable = True                
                walk_set_param_pub.publish(WALKING_STRAIGHT)
                walk_command_pub.publish('start')
                rospy.Rate(2).sleep()
                state = START_FORWARD
                
            elif state == START_FORWARD:
                WALKING_STRAIGHT.x_move_amplitude = 0.010
                WALKING_STRAIGHT.balance_enable = True
                walk_set_param_pub.publish(WALKING_STRAIGHT)
                walk_command_pub.publish('start')
                rospy.Rate(2).sleep()
                state = FORWARD
                
                   
            elif state == STOP_FORWARD:
                WALKING_STRAIGHT.x_move_amplitude = 0.010
                WALKING_STRAIGHT.angle_move_amplitude = turn * 0.5
                WALKING_STRAIGHT.balance_enable = True
                walk_set_param_pub.publish(WALKING_STRAIGHT)
                walk_command_pub.publish('start')
                rospy.Rate(2).sleep()
                state = STOP
                    
            elif state == STOP:
                walk_command_pub.publish('stop')
                rospy.Rate(2).sleep()
                state = START_BACKWARD
                
            elif state == START_BACKWARD:
                WALKING_STRAIGHT.x_move_amplitude = -0.015
                WALKING_STRAIGHT.init_z_offset = 0.05
                WALKING_STRAIGHT.y_move_amplitude = 0
                WALKING_STRAIGHT.angle_move_amplitude = 0 
                WALKING_STRAIGHT.balance_enable = True
                walk_set_param_pub.publish(WALKING_STRAIGHT)
                walk_command_pub.publish('start')
                rospy.Rate(2).sleep()
                '''
                WALKING_STRAIGHT.x_move_amplitude = -0.01
                WALKING_STRAIGHT.angle_move_amplitude = 0
                WALKING_STRAIGHT.balance_enable = True
                walk_set_param_pub.publish(WALKING_STRAIGHT)
                walk_command_pub.publish('start')
                rospy.Rate(2).sleep()
                '''
                state = BACKWARD
                
            #end if distince!=None

        
        else:
            rospy.loginfo('READY_MODE')
            not_found += 1
        # rospy.Rate(10).sleep()
        
        # cv2.imshow('image', frame)
        # rospy.loginfo('detect rate:' + str(found/(not_found+found)))
        
        
        rospy.loginfo('x_move: '+ str(WALKING_STRAIGHT.x_move_amplitude))
        rospy.loginfo('y_move: '+ str(WALKING_STRAIGHT.y_move_amplitude))
        rospy.loginfo('a_move: '+ str(WALKING_STRAIGHT.angle_move_amplitude/DEGREE2RADIAN))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

