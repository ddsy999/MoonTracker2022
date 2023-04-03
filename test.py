import cv2
import numpy as np


cap1 = cv2.VideoCapture('http://172.30.1.37:8081')
cap2 = cv2.VideoCapture('http://172.30.1.67:8080/video')
while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    frame2 = cv2.resize(frame2 , (640,480))
    frame2 = cv2.flip(frame2,0)
    if ret1:
        cv2.imshow('frame1',frame1)
        
    if ret2:
        cv2.imshow('frame2',frame2)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()

#sudo service motion restart
#sudo nano /etc/motion/motion.conf
#Thread /home/pi/webcam/cam.cam1.conf
#Thread /home/pi/webcam/cam.cam2.conf
