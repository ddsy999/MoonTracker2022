
#import re
import cv2
#import numpy as np
import paramiko
#import getpass
import cv2
from time import sleep
import rpyc
import datetime
#import dropbox
import os

#from functions import *
class constants:
    
    global VideoCaptureIP_
    global EV3IP_
    global Dropbox_appkey_
    global Dropbox_token_
    global RPYC_SERVER_PORT
    
    def __init__(self) :
            self.VideoCaptureIP_ = ""
            self.EV3IP_ = ""
            self.Dropbox_appkey_ = ""
            self.Dropbox_token_ = ""
            self.RPYC_SERVER_PORT = ""
            

            print(" [Start] excute constants.py")

            #f = open("gitignore_VideoCaptureIP.txt",'r')
            
            #self.VideoCaptureIP_ = f.readline()
            #f.close()

            #f = open("gitignore_EV3IP.txt",'r')
            #self.EV3IP_ = f.readline()
            #f.close()

            #f = open("gitignore_Dropbox_appkey.txt",'r')
            #self.Dropbox_appkey_ = f.readline()
            #f.close()

            #f = open("gitignore_Dropbox_token.txt",'r')
            #self.Dropbox_token_ = f.readline()
            #f.close()
            self.EV3IP_ = '172.30.1.18' # When Phone 192.168.103.49
            
            self.RPYC_SERVER_PORT = 18812
            self.VideoCaptureIP_ = 'http://172.30.1.37:8081'#'http://172.30.1.43:8081' #'http://192.168.103.78:8081'
            VideoCaptureIP_  = self.VideoCaptureIP_
            EV3IP_           = self.EV3IP_
            #Dropbox_appkey_  = self.Dropbox_appkey_
            #Dropbox_token_   = self.Dropbox_token_
            RPYC_SERVER_PORT = self.RPYC_SERVER_PORT
            
            print(" [End] excute constants.py")
    
    def timePrint(self , tictoc_ , interval)  :
        
        current_Time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        current_Year, current_Month, current_Day, current_Hour, current_Minute, current_Second = current_Time.split("_")

        if tictoc_== -1 : 
            tictoc_ = int(current_Second)
            return [int(current_Second) , 1 ]
        elif tictoc_ != int(current_Second) and int(current_Second)%interval ==0 :
            #print(int(current_Second)  )
            tictoc_ = int(current_Second)
            return [tictoc_ , 1 ]
        else : return [tictoc_ , 0 ]