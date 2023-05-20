import cv2
import numpy as np
from camClass import *
from pynput import keyboard


from buildhat import Motor
motorUD = Motor('C')
motorLR = Motor('D')

# 키 입력 이벤트 핸들러
def on_key_press(key):
    try:
        if key == keyboard.Key.esc:  # ESC 키 체크
            print('ESC 키를 눌러 프로그램을 종료합니다.')
            listener.stop()  # 리스너 중지
        elif key.char == 'a':
            print('a')
        elif key.char == 's':
            motorLR.run_for_seconds(5,speed=10)
            print('s')
        elif key.char == 'd':
            print('d')
        elif key.char == 'w':
            print('w')
    except AttributeError:
        pass
    
    
#0. Start 버튼 대기
user_input = input("시작하려면 아무 키나 입력하세요: ")
# 키 입력 이벤트 핸들러 등록
listener = keyboard.Listener(on_press=on_key_press)
listener.start()
print("시작합니다")


#1. cam 연결 시도
print("Cam 상태 확인 중")
try:
    computerCam = camClass(ip='http://localhost:8081', flip=False)
except:
    print("Cam 연결 실패")
finally:
    print("Cam 연결 성공: " + str(computerCam.captureValid))

user_input = input("Dual Cam을 시작하려면 q를 입력하세요: ")


#2. Dual Cam Window
if user_input == 'q':
    print("Dual Cam 시작")
    computerCam.show(maskedview=True)

    print("Dual Cam 종료")


#3. sv105 cam window 실행 & 자동추적
user_input = input("자동 추적을 시작하려면 q를 입력하세요: ")
if user_input == 'q':
    h_min, h_max, s_min, s_max, v_min, v_max = 93, 142, 128, 255, 49, 255
    computerCam.noCamDectect(h_min, h_max, s_min, s_max, v_min, v_max)

    

computerCam.release()
# 키 입력 이벤트 리스너 중지
listener.stop()
