
import cv2 
import numpy as np 
import keyboard
from camClass import *
import threading
#capturePiCam = cv2.VideoCapture('http://localhost:8081')
#captureSV105 = cv2.VideoCapture(1) #1은 SV105

##################################################
#0. Start 버튼 대기 
#1. cam 연결 시도 
#1-1. cam 연결 상태 print 
#2. cam Window Big and small
#2-1. 위치 조정 후 Dual 캠 종료
#3. sv105 cam window 실행 & 자동추적 
##################################################

def on_key_press(event):
    if event.name == 'a':
        print('a')
    if event.name == 's':
        print('s')
    if event.name == 'd':
        print('d')
    if event.name == 'w':
        print('w')


#0. Start 버튼 대기 
user_input = input("시작하려면 아무키나 입력하세요")
print("시작합니다")


#1. cam 연결 시도
#1-1. cam 연결 상태 print 
print("Cam 상태 확인중")
try:
    computerCam = camClass(ip=0,flip=False)
except:
    print("cam Failed")
finally:
    print("cam Success " + str(computerCam.captureValid))
    
user_input = input("Dual Cam을 시작하려면 s 를 입력하세요 ")

#2. Dual Cam Window
if user_input=='y' or user_input=='Y':
    print("Dual Cam 시작")
    computerCam.show(maskedview=True)
    #2-1. 위치 조정
    # 키 입력 이벤트 핸들러 등록
    keyboard.on_press(on_key_press)
    # 키 입력 이벤트 핸들러 제거
    keyboard.unhook_all()
    
print("Dual Cam 종료")
#3. sv105 cam window 실행 & 자동추적 
user_input = input("자동 추적을 시작하려면 s 를 입력하세요 ")
if user_input=='Y' or user_input=='y':
    h_min,h_max,s_min,s_max,v_min,v_max = 93,142,128,255,49,255

    computerCam.noCamDectect(h_min,h_max,s_min,s_max,v_min,v_max)

    computerCam.release()


