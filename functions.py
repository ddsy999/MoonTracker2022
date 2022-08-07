import cv2
import numpy as np
import paramiko
#import getpass
import cv2
from time import sleep
import rpyc
import datetime
#import dropbox
import os

# functions

def getContours(img , imgContour):
    
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
                cv2.rectangle(imgContour,((x,y),(x+w,y+h)),(0,255,0),2)
        
    except:
        #print("fail to getContours")
        return [ -1 , -1 , 0]
    return [ -1 , -1 , 0]    # object x , y , exist
    
def stackImages(imgArray,scale,lables=[]):
    sizeW= imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver



def empty(a):
    pass



def fileFound_and_DropBox(Dropbox_token , Dropbox_appkey):
    import os
    import dropbox

    dropbox_location = "/MoonCapture/capture/"
    Machine_location = "C:/Users/ddsy9/PycharmProjects/pythonProject6/venv/capture/"

    dbx = dropbox.Dropbox(oauth2_refresh_token=Dropbox_token,
                          app_key=Dropbox_appkey, timeout=900)

    file_list = os.listdir(Machine_location)
    print("fileList :",file_list)
    if len(file_list)>0:
        Machine_filename = Machine_location+file_list[0]
        dropbox_pathname = dropbox_location+file_list[0]

        with open(Machine_filename, "rb") as f:
            dbx.files_upload(f.read(), dropbox_pathname , mode=dropbox.files.WriteMode.overwrite)

        os.remove(Machine_filename)




def readTxtFile(fileNm):
    file = open(fileNm + ".txt", "r", encoding="UTF-8")

    data = []
    while (1):
        line = file.readline()

        try:
            escape = line.index('\n')
        except:
            escape = len(line)
        if line:
            data.append(line[0:escape])
        else:
            break
    file.close()

    return data


def execCommands(EV3IP_):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    cli.connect(EV3IP_, username="robot", password="maker")

    commandLines = readTxtFile("" + "venv/ev3_ssh_command")  # 메모장 파일에 적어놨던 명령어 텍스트 읽어옴
    print(commandLines)

    stdin, stdout, stderr = cli.exec_command(";".join(commandLines))  # 명령어 실행
    lines = stdout.readlines()  # 실행한 명령어에 대한 결과 텍스트
    resultData = ''.join(lines)

    print(resultData)  # 결과 확인


#execCommands()



