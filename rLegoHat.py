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
        if key == keyboard.Key.esc or key.char=='q':  # ESC 키 체크
            print('ESC Key : Keyboad Listener End')
            listener.stop()  # 리스너 중지
        elif key.char == 'a':
            motorLR.run_for_seconds(2,speed=-10)
        elif key.char == 's':
            motorUD.run_for_seconds(2,speed=-10)
        elif key.char == 'd':
            motorLR.run_for_seconds(2,speed=10)
        elif key.char == 'w':
            motorUD.run_for_seconds(2,speed=10)
    except AttributeError:
        pass
    
    
#0. Start 버튼 대기
user_input = input("Stat press Any Key ")
# 키 입력 이벤트 핸들러 등록
listener = keyboard.Listener(on_press=on_key_press)
listener.start()
print("Start")


#1. cam 연결 시도
print("Confirming Cam Status ")
try:
    piCam = camClass(ip='http://localhost:8081', flip=True,targetBox=True)
except:
    print("piCam Connect Fail")
finally:
    print("piCam Connet Succ: " + str(piCam.captureValid))
    
try:
    sv105Cam = camClass(ip=1, flip=False,width=640//4 , height=480//4)
except:
    print("sv105Cam Connect Fail")
finally:
    print("sv105Cam Connet Succ: " + str(sv105Cam.captureValid))
    

user_input = input("Dual Cam Start Press  q : ")


#2. Dual Cam Window
if user_input == 'q':
    print("Dual Cam Start")
    camClass.totalShow()
    print("Dual Cam End")



#3. sv105 cam window 실행 & 자동추적
#user_input = input("자동 추적을 시작하려면 q를 입력하세요: ")
#if user_input == 'q':
#    h_min, h_max, s_min, s_max, v_min, v_max = 93, 142, 128, 255, 49, 255
#    piCam.noCamDectect(h_min, h_max, s_min, s_max, v_min, v_max)

    

#piCam.release()
# 키 입력 이벤트 리스너 중지
listener.stop()
print('End')