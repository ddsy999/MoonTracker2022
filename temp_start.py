from buildhat import Motor  
motor = Motor('A')
motor.run_forever()



import cv2 
import numpy as np 
from picamera import PiCamera

capturePiCam = cv2.VideoCapture('http://localhost:8081')
captureSV105 = cv2.VideoCapture(1) #1은 SV105

capturePiCam.set(cv2.CAP_PROP_FRAME_WIDTH, 640//4)
capturePiCam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480//4)

captureSV105.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captureSV105.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret1, frame1 = capturePiCam.read()
    ret2, frame2 = captureSV105.read()
    cv2.imshow('video1', frame1)
    cv2.imshow('video2', frame2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
capturePiCam.release()
captureSV105.release()
cv2.destroyAllWindows()





from buildhat import Motor
motorUD = Motor('C')
motorLR = Motor('D')

# - left + right
# + Up   - Down 
motorLR.run_for_seconds(5,speed=10)







import cv2 
import numpy as np 
from picamera import PiCamera

#capturePiCam = cv2.VideoCapture('http://localhost:8081')
captureSV105 = cv2.VideoCapture(1) #1은 SV105

captureSV105.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captureSV105.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret2, frame2 = captureSV105.read()
    cv2.imshow('video', frame2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
captureSV105.release()
cv2.destroyAllWindows()




import cv2 
import numpy as np 
from picamera import PiCamera

capturePiCam = cv2.VideoCapture('http://localhost:8081')
#captureSV105 = cv2.VideoCapture(1) #1은 SV105

capturePiCam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capturePiCam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret1, frame1 = capturePiCam.read()
    cv2.imshow('video', frame1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
capturePiCam.release()
cv2.destroyAllWindows()


picam = camClass(ip='http://localhost:8081')


import cv2
import numpy as np
from picamera import PiCamera
from camClass import *

picam = camClass(ip='http://localhost:8081')
picam.show()

import cv2
import numpy as np
from picamera import PiCamera
from camClass import *

picam = camClass(ip='http://localhost:8081')
picam.show(gray=True,canny=True)



sv105Cam = camClass(ip=1,width=640,height=480)
piCam = camClass(ip='http://localhost:8081',width=640,height=480,fx=0.25,fy=0.25)
#picam.show(gray=True,canny=True)

camClass.totalShow()