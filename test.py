
import cv2
import numpy as np
from camClass import *
from time import sleep
picam = camClass(ip=0,gray=True,canny=True,filp=False)
picam.show()





import cv2
import numpy as np
import time 
import numpy as np

prev_time = time.time()

capturePiCam = cv2.VideoCapture(0)
ret, img = capturePiCam.read()
img = cv2.resize(img, (640   , 480))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
moonImg = cv2.imread('examplePhoto/moon1.jpg')
moonImg = cv2.resize(moonImg, (640   , 480))
concat_img = np.concatenate((moonImg, img), axis=1)
while True:
    curr_time = time.time()
    if curr_time - prev_time >= 5:
        # 두 번째 이미지 읽어들이기
        ret, img = capturePiCam.read()
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        moonImg = cv2.imread('examplePhoto/moon1.jpg')
        img = cv2.resize(img, (640   , 480))
        moonImg = cv2.resize(moonImg, (640   , 480))
        concat_img = np.concatenate((moonImg, img), axis=1)
        # 이전 시간 업데이트
        prev_time = curr_time
    cv2.imshow('Total', concat_img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        print("break")
        break
capturePiCam.release()

cv2.destroyAllWindows()



def getContours(img):
    #  contour를 찾는 func & option 규칙들 
    img_contour = np.zeros_like(img)
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_contour,contours,-1,(255,0,0),3,2)
    return img_contour


import cv2
import numpy as np
import time

prev_time = time.time()
capturePiCam = cv2.VideoCapture(0)

# moonImg를 RGB 형식으로 읽어들이기
moonImg = cv2.imread('examplePhoto/moon1.jpg', cv2.IMREAD_COLOR)
moonImg = cv2.resize(moonImg, (640, 480))



while True:
    curr_time = time.time()
    if curr_time - prev_time >= 5:
        # 두 번째 이미지 읽어들이기
        ret, img = capturePiCam.read()
        img = cv2.resize(img, (640, 480))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contour , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        #img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # img를 RGB로 변환
        #concat_img = np.concatenate((moonImg, img), axis=1)
        # 이전 시간 업데이트
        prev_time = curr_time
        img = getContours(img)
    cv2.imshow('Total', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        print("break")
        break

capturePiCam.release()
cv2.destroyAllWindows()




def getMaskedImg(img):
    #  contour를 찾는 func & option 규칙들 
    img_contour = np.zeros_like(img)
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_contour,contours,-1,(255,0,0),3,2)
    return img_contour






import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

capturePiCam = cv2.VideoCapture(0)
prev_time = 0

while True:
    # 카메라에서 이미지 읽기
    #ret, img = capturePiCam.read()
    img = cv2.imread('examplePhoto/moon1.jpg')
    img = cv2.resize(img, (640, 480))
    img = cv2.flip(img, 1)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGray = cv2.GaussianBlur(imgGray,(7,7),1)
    
    # 이미지를 HSV 색 공간으로 변환
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 트랙바로부터 HSV 값 범위를 읽어들임
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    # 범위 내의 색상만을 갖는 마스크 이미지 생성
    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower_range, upper_range)
    
    # 마스크 이미지에서 윤곽선 찾기
    contour, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # 윤곽선을 기준으로 객체 경계를 그림
    cv2.drawContours(img, contour, -1, (255,0,0), 3)
    
    # 이미지 출력
    cv2.imshow("Frame", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Gray", imgGray)
    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 객체와 창 종료
capturePiCam.release()
cv2.destroyAllWindows()



# 1. Img HSV 변환  Masked Value > 100 
# 2. MaskedImg 에서 Contour 찾기 


def HSVandMasked(img,h_min = 0,h_max = 179,s_min = 0,s_max = 255,v_min = 0,v_max = 255):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower_range, upper_range)
    return mask
    

def getContourImg(img,target=True,areaMin=0):
    # contour를 찾는 func & option 규칙들 
    img_contour = np.zeros_like(img)
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if target == True:
        for cnt in contours:
            areaCnt = cv2.contourArea(cnt)
            print("area is "+areaCnt)
            if areaCnt > areaMin:
                M = cv2.moments(cnt)
                # Contour의 중심점 계산
                if M['m00'] == 0:
                    # contour 면적이 0인 경우
                    continue
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
            else:
                pass
    cv2.drawContours(img_contour,contours,-1,(255,0,0),3,2)
    return img_contour,cx,cy


    
import cv2
import numpy as np


while True:
    # 카메라에서 이미지 읽기
    #ret, img = capturePiCam.read()
    img = cv2.imread('examplePhoto/moon1.jpg')
    img = cv2.resize(img, (640, 480))

    imgDetect = HSVandMasked(img,v_min=100)
    imgDetect,cx,cy = getContourImg(imgDetect)
    
    # 이미지 출력
    img = cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
    cv2.imshow("Frame", img)
    cv2.imshow("imgDetect", imgDetect)
    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 객체와 창 종료
cv2.destroyAllWindows()


    
import cv2
import numpy as np
from camClass import *
computerCam = camClass(ip=0,flip=False)
computerCam.show(masked=True)





import cv2
import numpy as np
from camClass import *
computerCam = camClass(ip=0,flip=False)

h_min,h_max,s_min,s_max,v_min,v_max = 93,142,128,255,49,255
while True:
    computerCam.noCamDectect(h_min,h_max,s_min,s_max,v_min,v_max)
    print(computerCam.cx,computerCam.cy)


