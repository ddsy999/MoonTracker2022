import cv2
import numpy as np


cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while(True):
    ret1, frame1 = cap1.read()
    cv2.imshow('frame',frame1)
    ret2, frame2 = cap2.read()
    cv2.imshow('frame',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()