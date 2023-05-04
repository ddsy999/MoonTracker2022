import cv2
import numpy as np
from camClass import camClass

cam1 = camClass(ip='http://172.30.1.24:8081')

cam1.show(canny=True)

import picamera 
import picamera.array 

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24


output = picamera.array.PiRGBArray(camera, size=camera.resolution)
camera.start_preview()
while True:
    # 캡처한 이미지를 PiRGBArray에 저장
    camera.capture(output, 'rgb')
    # PiRGBArray를 OpenCV의 Mat 형식으로 변환
    frame = output.array
    cv2.imshow('image', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    output.truncate(0)
camera.stop_preview()