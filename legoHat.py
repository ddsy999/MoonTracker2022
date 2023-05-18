
import cv2 
import numpy as np 
import keyboard
from camClass import *
import threading
#capturePiCam = cv2.VideoCapture('http://localhost:8081')
#captureSV105 = cv2.VideoCapture(1) #1은 SV105


computerCam = camClass(ip=0,flip=False)

computerCam.show(masked=True)

# Blue 
h_min,h_max,s_min,s_max,v_min,v_max = 93,142,128,255,49,255

computerCam.noCamDectect(h_min,h_max,s_min,s_max,v_min,v_max)

computerCam.release()