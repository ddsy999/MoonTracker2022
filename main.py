
# opencv-python     4.5.4.60


import cv2
import numpy as np
import paramiko
#import getpass
import cv2
from time import sleep
import rpyc
import datetime
import time
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
Window_Width , Window_Height     = 640  , 480
Object_x , Object_y ,ObjectExist = 0 , 0 , 0
tictoc                           = -1 # default value : -1 
timeEvent                        = 1 
UpDown_time = 2000
LeftRight_time = 2000
UpDown_Speed = 500
LeftRight_Speed = 500
moveKey = [ord("a"),ord("d"),ord("s"),ord("w")]

moveSlowRateTime  = 4
moveSlowRateSpeed = 2
autoSlowRateTime  = 10
autoSlowRateSpeed = 5

targetBoxRate = 4
targetBox_Width = Window_Width/targetBoxRate
targetBox_Height = Window_Height/targetBoxRate
targetBox_WidthMidPoint  = Window_Width/2
targetBox_HeightMidPoint = Window_Height/2
targetBox = (int(targetBox_WidthMidPoint-targetBox_Width/2),int(targetBox_HeightMidPoint-targetBox_Height/2)),(int(targetBox_WidthMidPoint+targetBox_Width/2),int(targetBox_HeightMidPoint+targetBox_Height/2))

targetBoxLeftMagin , targetBoxRightMagin = min(targetBox[1][0],targetBox[0][0]) , max(targetBox[1][0],targetBox[0][0])
targetBoxUpMagin , targetBoxDownMagin    = min(targetBox[1][1],targetBox[0][1]) , max(targetBox[1][1],targetBox[0][1])


try:
    # Home Wifi
    Lego = ev3_connect(EV3IP_ , RPYC_SERVER_PORT )
    capture = cv2.VideoCapture(VideoCaptureIP_)
except:
    # Mobile
    Lego = ev3_connect('192.168.103.49', RPYC_SERVER_PORT )
    capture = cv2.VideoCapture('http://192.168.103.78:8081')


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
    img = cv2.resize(img , (Window_Width,Window_Height))
    # img = cv2.flip(img,0)
    # Original Image 
    
    
    #cv2.imshow("livestream",img)

    imgContour = img.copy()
    imgContour = cv2.rectangle(imgContour,targetBox[0],targetBox[1],(0,255,0),2)
    # Gray Image
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray",imgGray)

    # GrayBlur Image
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

    # Canny Imags
    imgCanny = cv2.Canny(imgBlur,100,100)
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
    cv2.imshow("MaskCanny", imgMaskCanny)

    Object_x , Object_y , ObjectExist = getContours(imgMaskCanny , imgContour)


    cv2.imshow("Contour",imgContour)



    tictoc , timeEvent = constants_.timePrint(tictoc_ = tictoc , interval=2)
    
    
    inputKey = cv2.waitKey(1)
    
    if inputKey in moveKey:
        # if KeyBoard Move 
            if inputKey == ord("a") :
                Lego.MotorLR(speed_= -LeftRight_Speed/moveSlowRateSpeed, time_ = LeftRight_time/moveSlowRateTime)
            elif inputKey == ord("d") :
                Lego.MotorLR(speed_= LeftRight_Speed/moveSlowRateSpeed, time_ = LeftRight_time/moveSlowRateTime)
    
                
            if inputKey == ord("w"):
                Lego.MotorUD(speed_ = -UpDown_Speed/moveSlowRateSpeed, time_ = UpDown_time/moveSlowRateTime)
            elif inputKey == ord("s"):
                Lego.MotorUD(speed_ = UpDown_Speed/moveSlowRateSpeed, time_ = UpDown_time/moveSlowRateTime)
    else :
        if ObjectExist and timeEvent: 
            print('tictoc : {tictoc} timeEvent : {timeEvent} ObjectExist : {ObjectExist}'.format(tictoc=tictoc,timeEvent=timeEvent,ObjectExist=ObjectExist))
            print(Object_x , Object_y )
        # if ObjectExist and Lego.ev3connect : # When Object in Screen & Ev3 Connect on

            if (Object_x - targetBoxRightMagin)  > 0 :
                print("auto Move R")
                Lego.MotorLR(speed_= LeftRight_Speed/autoSlowRateSpeed, time_ = LeftRight_time/autoSlowRateTime)
            elif (Object_x - targetBoxLeftMagin) < 0 :
                print("auto Move L")
                Lego.MotorLR(speed_= -LeftRight_Speed/autoSlowRateSpeed, time_ = LeftRight_time/autoSlowRateTime)
    
                
            if (Object_y - targetBoxUpMagin ) < 0 :
                print("auto Move U")
                Lego.MotorUD(speed_ = -UpDown_Speed/autoSlowRateSpeed, time_ = UpDown_time/autoSlowRateTime)
            elif (Object_y - targetBoxDownMagin) > 0 :
                print("auto Move D")
                Lego.MotorUD(speed_ = UpDown_Speed/autoSlowRateSpeed, time_ = UpDown_time/autoSlowRateTime)

            
    if inputKey == ord("c"):
        now = time
        now_string = now.strftime("%Y%m%d_%H_%M_%S")
        cv2.imwrite(os.getcwd()+'\\Image_'+now_string+'.png',img)         
    
    if inputKey == ord("q"):
        capture.release()
        cv2.destroyAllWindows()
        break



