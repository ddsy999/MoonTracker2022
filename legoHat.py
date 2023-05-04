from buildhat import Motor  
motor = Motor('A')
motor.run_forever()



import cv2 
import numpy as np 
from picamera import PiCamera

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

from buildhat import Motor
motorUD = Motor('C')
motorLR = Motor('D')

# - left + right
# + Up   - Down 
motorLR.run_for_seconds(5,speed=10)
