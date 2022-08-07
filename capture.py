# opencv-python     4.5.4.60

import cv2
import numpy as np
#import paramiko
import getpass
from time import sleep
import rpyc
import datetime
#import dropbox
import os


# Variable

Window_Width  = 640
Window_Heigth = 360
Object_x = 0
Object_y = 0
ObjectExist = 0
tictic = -1
ev3connect = 0 # 0 is not conn / 1 is conn
previous_second = -1

from functions import *
from constants import *

VideoCaptureIP_  = constants().VideoCaptureIP_
EV3IP_           = constants().EV3IP_
Dropbox_appkey_  = constants().Dropbox_appkey_
Dropbox_token_   = constants().Dropbox_token_
RPYC_SERVER_PORT = constants().RPYC_SERVER_PORT



#capture = cv2.VideoCapture('rtsp://js:aaa@192.168.0.177:5554/sss')
#capture = cv2.VideoCapture(VideoCaptureIP_)
#capture = cv2.VideoCapture('https://192.168.219.200:8080/video')
capture = cv2.VideoCapture('rtsp://192.168.0.177:5554')


while True:

    ObjectExist = 0

    
    current_Time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    current_Year, current_Month, current_Day, current_Hour, current_Minute, current_Second = current_Time.split("_")

    if tictic == -1 : tictic = int(current_Second)
    elif tictic != int(current_Second) and int(current_Second)%10 == 0 : 
        print('time ' + current_Second) 
        tictic = int(current_Second)

    # img Read
    _ , img = capture.read()
    img = cv2.resize(img , (Window_Width,Window_Heigth))
    #img = cv2.flip(img,0)
    # Original Image
    cv2.imshow("livestream",img)
    
    # k = cv2.waitKey(0)
    # if k == 27: # esc key
    #     cv2.destroyAllWindow()
    # elif k == ord('s'): # 's' key
    #     cv2.imwrite('testgray.png',img)
    #     cv2.destroyAllWindow()
    if cv2.waitKey(1) == ord("q"):
        break
