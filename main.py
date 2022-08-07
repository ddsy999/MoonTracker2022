
# opencv-python     4.5.4.60


import cv2
import numpy as np
import paramiko
#import getpass
import cv2
from time import sleep
import rpyc
import datetime
#import dropbox
import os

from functions import *

from constants import *

from ev3_connect import *

# constants
constants_ = constants()


VideoCaptureIP_                  = constants_.VideoCaptureIP_
EV3IP_                           = constants_.EV3IP_
#Dropbox_appkey_                  = constants_.Dropbox_appkey_
#Dropbox_token_                   = constants_.Dropbox_token_
RPYC_SERVER_PORT                 = constants_.RPYC_SERVER_PORT
Window_Width , Window_Heigth     = 640  , 360
Object_x , Object_y ,ObjectExist = 0 , 0 , 0
tictoc                           = -1 # default value : -1 
timeEvent                        = 1 

try:
    Lego = ev3_connect(EV3IP_ , RPYC_SERVER_PORT )
    capture = cv2.VideoCapture(VideoCaptureIP_)
except:
    Lego = ev3_connect('192.168.103.49', RPYC_SERVER_PORT )
    capture = cv2.VideoCapture('http://192.168.103.78:8081')
#capture = cv2.VideoCapture(VideoCaptureIP_)
#capture = cv2.VideoCapture("http://192.168.0.108:8081")


#cv2.namedWindow("TrackBars")
#cv2.resizeWindow("TrackBars", 640 , 640)
#cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
#cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
#cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
#cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
#cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
#cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)





while True :

    # img Read
    _ , img = capture.read()
    img = cv2.resize(img , (Window_Width,Window_Heigth))
    # img = cv2.flip(img,0)
    # Original Image 
    
    
    cv2.imshow("livestream",img)

    imgContour = img.copy()
    imgContour = cv2.rectangle(imgContour,(int(Window_Width/2-50),int(Window_Heigth/2-50)),(int(Window_Width/2+50),int(Window_Heigth/2+50)),(0,255,0),2)
    # Gray Image
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray",imgGray)

    # GrayBlur Image
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    # Canny Imags
    imgCanny = cv2.Canny(imgBlur,50,50)
    #cv2.imshow("Canny", imgCanny)


    # HSV Image
    imgHSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    #cv2.imshow("livestreamHSV",imgHSV)



    # temp
    # h_min,h_max,s_min,s_max,v_min,v_max
    h_min,h_max,s_min,s_max,v_min,v_max = 93,142,128,255,49,255
    HSV_lower = np.array([h_min,s_min,v_min])
    HSV_upper = np.array([h_max,s_max,v_max])


    imgMask = cv2.inRange(imgHSV , HSV_lower , HSV_upper)

    # HSV Mask Image
    #cv2.imshow("livestreamHSV_MASK", imgMask)

    # bitwise Image
    imgbitwise = cv2.bitwise_and(imgBlur,imgBlur,mask = imgMask)
    #cv2.imshow("bitMask",imgbitwise)

    # bitwise Canny
    imgMaskCanny = cv2.Canny(imgbitwise, 100, 100)
    #cv2.imshow("MaskCanny", imgMaskCanny)

    Object_x , Object_y , ObjectExist = getContours(imgMaskCanny , imgContour)


    #cv2.imshow("Contour",imgContour)



    tictoc , timeEvent = constants_.timePrint(tictoc_ = tictoc , interval=2)
    
    if ObjectExist and timeEvent: 
        print('tictoc : {tictoc} timeEvent : {timeEvent} ObjectExist : {ObjectExist}'.format(tictoc=tictoc,timeEvent=timeEvent,ObjectExist=ObjectExist))
        print(Object_x , Object_y )
    # if ObjectExist and Lego.ev3connect : # When Object in Screen & Ev3 Connect on

        if (Object_x - Window_Width/2)>100 :
            Lego.MotorLR(speed_= -30, time_ = 500)
        elif (Object_x - Window_Width/2)<-100 :
            Lego.MotorLR(speed_= 30, time_ = 500)
 
            
        if (Object_y - Window_Heigth / 2) <-50:
            Lego.MotorUD(speed_ = -300, time_ = 1000)
        elif (Object_y - Window_Heigth / 2) > 50:
            Lego.MotorUD(speed_ = 300, time_ = 1000)

            
            
    
    if cv2.waitKey(1) == ord("q"):
        capture.release()
        cv2.destroyAllWindows()
        break
    















