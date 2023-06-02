import cv2
import numpy as np
from camClass import *
from pynput import keyboard
from buildhat import Motor

print('Motor Loading')
motorUD = Motor('C')
motorLR = Motor('D')
# - left + right
# + Up   - Down 

# 키 입력 이벤트 핸들러
def on_key_press(key):
    try:
        if key == keyboard.Key.esc :  # ESC 키 체크
            print('ESC Key : Keyboad Listener End')
            listener.stop()  # 리스너 중지
        elif key.char == 'a':
            motorLR.run_for_seconds(1,speed=-10)
        elif key.char == 's':
            motorUD.run_for_seconds(1,speed=-10)
        elif key.char == 'd':
            motorLR.run_for_seconds(1,speed=20)
        elif key.char == 'w':
            motorUD.run_for_seconds(1,speed=20)
    except AttributeError:
        pass
    
    
#0. Start 버튼 대기
user_input = input("Stat press Any Key ")

print("Start")


# #1. cam 연결 시도
# print("Confirming Cam Status ")
# try:
#     HSVListValue = [93,142,128,255,49,255]
#     sv105Cam = camClass(ip=1,flip=False,HSVList=HSVListValue,contourMasked=False,targetBox=True)
#     piCam = camClass(ip='http://localhost:8081',flip=False,HSVList=HSVListValue,contourMasked=False)
#     print("piCam Connet Succ: " + str(piCam.captureValid))
#     print("sv105Cam Connet Succ: " + str(sv105Cam.captureValid))
# except:
#     print("piCam Connect Fail")

# user_input = input("Dual Cam Start Press  q : ")


# #2. Dual Cam Window
# if user_input == 'q':
#     print("Dual Cam Start")
#     camClass.totalShow()
#     print("Dual Cam End")
# else :
#     pass



#1. cam connect
#1-1. cam connect print 

print("Confirming Cam Status")
try:
    HSVListValue = [93,142,128,255,49,255]
    sv105Cam = camClass(ip=1,flip=False,HSVList=HSVListValue,contourMasked=False,targetBox=True)
    piCam = camClass(ip='http://localhost:8081',flip=False,HSVList=HSVListValue,contourMasked=False)
except:
    print("cam Failed")
finally:
    print("sv105Cam Success " + str(sv105Cam.captureValid)+" "+str(sv105Cam.textName))
    print("piCam Success " + str(piCam.captureValid)+" "+str(piCam.textName))
    
user_input = input("Cam sv105 Press 'v' or Cam Picam Press 'p' ")

while True:
     # 키 입력 대기
    print('while')
    if user_input == 'v':
        print('press v')
        print("valid sv105Cam "+ str(sv105Cam.captureValid))
        sv105Cam.show()
        user_input = input("Cam sv105 Press 'v' or Cam Picam Press 'p' ")
        
    elif user_input == 'p':
        print('press p')
        print("valid piCam "+ str(piCam.captureValid))
        piCam.show()
        user_input = input("Cam sv105 Press 'v' or Cam Picam Press 'p' ")
        
    if user_input == 'q': 
        break

    

#3. sv105 cam window 실행 & 자동추적
#user_input = input("자동 추적을 시작하려면 q를 입력하세요: ")
#if user_input == 'q':
#    h_min, h_max, s_min, s_max, v_min, v_max = 93, 142, 128, 255, 49, 255
#    piCam.noCamDectect(h_min, h_max, s_min, s_max, v_min, v_max)

    

# 키 입력 이벤트 핸들러 등록
listener = keyboard.Listener(on_press=on_key_press)
listener.start()
# 키 입력 이벤트 리스너 중지
listener.stop()
print('End')
