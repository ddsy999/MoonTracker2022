
import cv2 


def isFlip(img,filp):
    if filp :
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

def getContours(img , imgContour):
    import cv2
    try:
        global Object_x , Object_y , ObjectExist
        contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            #print(area)
            if area > 2000:
                cv2.drawContours(imgContour , cnt , -1 , (255,0,0),3)
                peri = cv2.arcLength(cnt,True)
                #print(peri)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True )
                objCor = len(approx)
                x,y,w,h = cv2.boundingRect(approx)
                x,y,w,h = int(x),int(y),int(w),int(h) 
                #print(['Edge', 'Width coord', 'Height coord'])
                #print([len(approx), (x + w/2) , (y + h/2)])
                cv2.circle(imgContour,(int(x + w/2) , int(y + h/2)) ,2, (0,0,255),cv2.FILLED)
                Object_x = (x + w/2)
                Object_y = (y + h/2)
                if len(approx)>=6 :
                    ObjectExist = 1
                return [Object_x , Object_y , 1]
    except:
        #print("fail to getContours")
        return [ -1 , -1 , 0]
    return [ -1 , -1 , 0]    # object x , y , exist
    
class camClass : 
    numOfcamClass = 0
    instances =[]
    def __init__(self,ip,width=640,height=480,fx=1,fy=1,filp=True,gray=False,canny=False) :    
        import cv2 
        camClass.numOfcamClass +=1 
        self.ip = ip
        self.width = width 
        self.height = height 
        self.fx = fx
        self.fy = fy
        self.gray = gray
        self.filp = filp
        self.canny = canny
        self.textName = "camClass_" + str(camClass.numOfcamClass)
        self.capture = cv2.VideoCapture(self.ip)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.captureValid = self.capture.isOpened()
        
        self.targetBoxWidthMidPoint  = self.width/2
        self.targetBoxHeightMidPoint = self.height/2
        self.targetBox = (int(self.targetBoxWidthMidPoint-self.width/2),int(self.targetBoxHeightMidPoint-self.height/2)),(int(self.targetBoxWidthMidPoint+self.width/2),int(self.targetBoxHeightMidPoint+self.height/2))
        camClass.instances.append(self)

    def show(self):
        import cv2 
        while True and self.captureValid:
            inputKey = cv2.waitKey(1)
            ret, frame = self.capture.read()
            frame = isResize(frame,self.fx,self.fy)
            frame = isFlip(frame,self.filp)
            frame = isGray(frame,self.gray)
            frame = isCanny(frame,self.canny)
            if ret:
                cv2.imshow(self.textName, frame)
                if inputKey == ord("q") or inputKey == ord("Q"):
                    self.capture.release()
                    cv2.destroyAllWindows()
                    break
            else:
                print("Error: Failed to capture video stream "+self.ip)
                break
        if not self.captureValid :
            print("Error: fail to VideoCapture "+self.ip)
            
    def fittingCaptureRead(self,frame):
        frame = isResize(frame,self.fx,self.fy)
        frame = isFlip(frame,self.filp)
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