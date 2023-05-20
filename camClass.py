
import cv2 


def isFlip(img,flip):
    if flip :
        return cv2.flip(img,0)
    else :
        return img
def isGray(img,gray):
    if gray :
        return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else :
        return img

def isResize(img,fxInput,fyInput):
    return cv2.resize(img, (0,0), fx=fxInput, fy=fyInput)

def isCanny(img,gray):
    if gray :
        return cv2.Canny(img,100,100)
    else :
        return img

def HSVandMasked(img,h_min = 0,h_max = 179,s_min = 0,s_max = 255,v_min = 0,v_max = 255):
    import numpy as np
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower_range, upper_range)
    return mask
    

def getContourImg(img,target=True,areaMin=0):
    import numpy as np
    # contour를 찾는 func & option 규칙들 
    img_contour = np.zeros_like(img)
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cx,cy= 0,0
    if target == True:
        for cnt in contours:
            areaCnt = cv2.contourArea(cnt)
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


    
class camClass : 
    numOfcamClass = 0
    instances =[]
    def __init__(self,ip,width=640,height=480,fx=1,fy=1,flip=True,gray=False,canny=False,area=500) :    
        import cv2 
        import time 
        camClass.numOfcamClass +=1 
        self.ip = ip
        self.width = width 
        self.height = height 
        self.fx = fx
        self.fy = fy
        self.gray = gray
        self.flip = flip
        self.canny = canny
        self.textName = "camClass_" + str(camClass.numOfcamClass)
        self.capture = cv2.VideoCapture(self.ip)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.captureValid = self.capture.isOpened()
        self.prevtime = time.time()
        self.moveKey = {"left":ord("a"),"right":ord("d"),"down":ord("s"),"up":ord("w") }
        self.cx = width/2
        self.cy = height/2
        self.area = area
        self.frame = None 
        
        self.targetBoxWidthMidPoint  = self.width/2
        self.targetBoxHeightMidPoint = self.height/2
        self.targetBox = (int(self.targetBoxWidthMidPoint-self.width/2),int(self.targetBoxHeightMidPoint-self.height/2)),(int(self.targetBoxWidthMidPoint+self.width/2),int(self.targetBoxHeightMidPoint+self.height/2))
        camClass.instances.append(self)

    def show(self,maskedview=True,value_min=100,HSVvalue = [93,142,128,255,49,255] ):
        import cv2 
        import keyboard
        while True and self.captureValid:
            inputKey = cv2.waitKey(1)
            ret, frame = self.capture.read()
            frame = self.fittingCaptureRead(frame)
            
            # Get Contour (HSV and Masked and Contour)
            
            # Blue Color Setting 
            h_min,h_max,s_min,s_max,v_min,v_max = HSVvalue
            
            # Value 100 
            # h_min,h_max,s_min,s_max,v_min,v_max = 0,179,0,255,100,255
            
            # Detecting Object
            imgDetect,cx,cy = self.detectObject(frame,h_min,h_max,s_min,s_max,v_min,v_max)
            frame = cv2.circle(frame, (self.cx,self.cy), 5, (0, 0, 255), -1)
            
            if ret:
                cv2.imshow(self.textName, frame)
                if maskedview==True:
                    cv2.imshow(self.textName+" Detect", imgDetect)
                    
                if inputKey == ord("q") or inputKey == ord("Q"):
                    #self.capture.release()
                    cv2.destroyAllWindows()
                    break
            else:
                print("Error: Failed to capture video stream "+str(self.ip))
                break
            
        if not self.captureValid :
            print("Error: fail to VideoCapture "+str(self.ip))

    def release(self):
        self.capture.release()
        cv2.destroyAllWindows()
        
    def noCamDectect(self,h_min,h_max,s_min,s_max,v_min,v_max ) :
        import keyboard
        import time
        #self.capture = cv2.VideoCapture(self.ip)
        while True: # Detected Object
            ret, frame = self.capture.read()
            frame = self.fittingCaptureRead(frame)
            imgDetect = HSVandMasked(frame,h_min,h_max,s_min,s_max,v_min,v_max)
            imgDetect,cx,cy = getContourImg(imgDetect,target=True,areaMin=self.area)    
            self.cx = cx # width
            self.cy = cy # height
            print(cx,cy)
            time.sleep(1)
            if keyboard.is_pressed('esc'):
                break

    
    def detectObject(self,frame,h_min,h_max,s_min,s_max,v_min,v_max ):
        # Detected Object
        frame = self.fittingCaptureRead(frame)
        imgDetect = HSVandMasked(frame,h_min,h_max,s_min,s_max,v_min,v_max)
        imgDetect,cx,cy = getContourImg(imgDetect,target=True,areaMin=self.area)    
        self.cx = cx # width
        self.cy = cy # height
        return(imgDetect,cx,cy)
    
    def fittingCaptureRead(self,frame):
        frame = isResize(frame,self.fx,self.fy)
        frame = isFlip(frame,self.flip)
        frame = isGray(frame,self.gray)
        frame = isCanny(frame,self.canny)
        return frame
    
    @classmethod
    def totalShow(cls):
        import cv2 
        while True:
            inputKey = cv2.waitKey(1)
            for instanceImg in cls.instances:
                ret, frame = instanceImg.capture.read()
                frame = instanceImg.fittingCaptureRead(instanceImg)
                cv2.imshow(instanceImg.textName, frame)

            if inputKey == ord("q") or inputKey == ord("Q"):
                for instanceImg in cls.instances:
                    instanceImg.capture.release()
                cv2.destroyAllWindows()
                break
            
class moveClass:
    def __init__(self,UDport='C',LRport='D',speed=10) :
        from buildhat import Motor
        self.motorUD = Motor('C')
        self.motorLR = Motor('D')
        self.speed=speed
        
    def Up(self,sec):
        self.motorUD.run_for_seconds(sec,speed=self.speed)
    def Down(self,sec):
        self.motorUD.run_for_seconds(sec,speed=-self.speed)
    def Right(self,sec):
        self.motorLR.run_for_seconds(sec,speed=self.speed)
    def Left(self,sec):
        self.motorLR.run_for_seconds(sec,speed=-self.speed)