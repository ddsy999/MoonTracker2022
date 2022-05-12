import cv2
import numpy as np
import paramiko
import getpass
import cv2
from time import sleep
import rpyc
import datetime
import dropbox
import os

f = open("gitignore_VideoCaptureIP.txt",'r')
VideoCaptureIP_ = f.readline()
f.close()

f = open("gitignore_EV3IP.txt",'r')
EV3IP_ = f.readline()
f.close()

f = open("gitignore_Dropbox_appkey.txt",'r')
Dropbox_appkey_ = f.readline()
f.close()

f = open("gitignore_Dropbox_token.txt",'r')
Dropbox_token_ = f.readline()
f.close()

RPYC_SERVER_PORT = 18812

#capture = cv2.VideoCapture('rtsp://js:aaa@192.168.0.177:5554/sss')
capture = cv2.VideoCapture(VideoCaptureIP_)

while True:

    ObjectExist = 0

    current_Time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    current_Year, current_Month, current_Day, current_Hour, current_Minute, current_Second = current_Time.split("_")

    tictic = int(current_Second)

    print('time ' + current_Second)

    # img Read
    _ , img = capture.read()
    #img = cv2.resize(img , (Window_Width,Window_Heigth))
    img = cv2.flip(img,0)
    # Original Image
    cv2.imshow("livestream",img)