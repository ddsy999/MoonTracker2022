



import paramiko
import getpass




#python3 /usr/local/bin/rpyc_classic.py -m threaded --host 0.0.0.0

import cv2
import numpy as np
from time import sleep
import rpyc
import datetime
import dropbox
import os

from functions import *

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



cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
server = EV3IP_ #= input("Server: ")  # 호스트명이나 IP 주소
user = 'robot'  #= input("Username: ")  
pwd = 'maker'   #= getpass.getpass("Password: ") # 암호입력 숨김

cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
cli.connect(EV3IP_, port = 22,  username=user, password=pwd)
stdin, stdout, stderr = cli.exec_command("python3 /usr/local/bin/rpyc_classic.py -m threaded --host 0.0.0.0")
#lines = stdout.readlines()
#print(''.join(lines))
 
cli.close()


def getContours(img):
    
    try:
        global Object_x , Object_y , ObjectExist
        contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            #print(area)
            if area > 2000:
                cv2.drawContours(imgContour , cnt , -1 , (255,0,0),3)
                peri = cv2.arcLength(cnt,True)
                #print(peri)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True )
                objCor = len(approx)
                x,y,w,h = cv2.boundingRect(approx)
                print(['Edge', 'Width coord', 'Height coord'])
                print([len(approx), (x + w/2) , (y + h/2)])
                cv2.circle(imgContour,(int(x + w/2) , int(y + h/2)) ,2, (0,0,255),cv2.FILLED)
                Object_x = (x + w/2)
                Object_y = (y + h/2)
                if len(approx)>=6 :
                    ObjectExist = 1

                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
    except:
        print("fail to getContours")


# Variable

Window_Width  = 640
Window_Heigth = 360
Object_x = 0
Object_y = 0
ObjectExist = 0
tictic = 0
ev3connect = 0 # 0 is not conn / 1 is conn
RPYC_SERVER_PORT = 18812
previous_second = -1




capture = cv2.VideoCapture(VideoCaptureIP_)



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640 , 640)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)







# EV3

# ev3connect
# 0 is not conn / 1 is conn
try:
    conn = rpyc.classic.connect( EV3IP_ , port=RPYC_SERVER_PORT)
    ev3 = conn.modules['ev3dev.ev3'] # import ev3dev.ev3 remotely
    m_updown = ev3.LargeMotor('outA')
    m_leftright = ev3.LargeMotor('outB')
    ev3_screen = ev3.Screen()
    ev3_screen.draw.text((30,30),"Connect")
    ev3_screen.update()


    ev3_sound = ev3.Sound()
    ev3_sound.beep()

    ev3connect = 1
except:
    print("EV3 Err")
    ev3connect = 0





while True:

    ObjectExist = 0

    current_Time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    current_Year, current_Month, current_Day, current_Hour, current_Minute, current_Second = current_Time.split("_")

    tictic = int(current_Second)

    print('time ' + current_Second)

    # img Read
    _ , img = capture.read()
    img = cv2.resize(img , (Window_Width,Window_Heigth))
    img = cv2.flip(img,0)
    # Original Image
    cv2.imshow("livestream",img)

    imgContour = img.copy()
    imgContour = cv2.rectangle(imgContour,(Window_Width/2-50,Window_Heigth/2-50),(Window_Width/2+50,Window_Heigth/2+50),(0,255,0),2)
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
    cv2.imshow("livestreamHSV",imgHSV)


    # HSV setting
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #print(h_min,h_max,s_min,s_max,v_min,v_max)

    # temp
    # h_min,h_max,s_min,s_max,v_min,v_max
    h_min,h_max,s_min,s_max,v_min,v_max = 93,142,128,255,49,255


    HSV_lower = np.array([h_min,s_min,v_min])
    HSV_upper = np.array([h_max,s_max,v_max])


    imgMask = cv2.inRange(imgHSV , HSV_lower , HSV_upper)

    # HSV Mask Image
    cv2.imshow("livestreamHSV_MASK", imgMask)

    # bitwise Image
    imgbitwise = cv2.bitwise_and(imgBlur,imgBlur,mask = imgMask)
    cv2.imshow("bitMask",imgbitwise)

    # bitwise Canny
    imgMaskCanny = cv2.Canny(imgbitwise, 100, 100)
    cv2.imshow("MaskCanny", imgMaskCanny)

    getContours(imgMaskCanny)


    cv2.imshow("Contour",imgContour)



    if tictic%1==0 and ObjectExist ==1 and tictic!=previous_second:

        cv2.imwrite('capture/' + 'opencv_' + current_Time +'_'+ 'X' + str(int(Object_x)) +'_' +'Y' + str(int(Object_y)) + '.png', img)

        if ev3connect==1 :
            if (Object_x - Window_Width/2)<-100 :
                m_leftright.run_timed(speed_sp=100, time_sp=400)
                print("Move leftright")
            if (Object_x - Window_Width/2)>100 :
                m_leftright.run_timed(speed_sp=-100, time_sp=400)
                print("Move leftright")
            if (Object_y - Window_Heigth / 2) > 50:
                m_updown.run_timed(speed_sp=-100, time_sp=400)
                print("Move updown")
            if (Object_y - Window_Heigth / 2) <-50:
                m_updown.run_timed(speed_sp=100, time_sp=400)
                print("Move updown")
    previous_second = tictic

    if cv2.waitKey(1) == ord("q"):
        break




capture.release()
cv2.destroyAllWindows()





