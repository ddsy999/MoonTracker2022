
import cv2
import numpy as np
import paramiko
import getpass
import cv2
from time import sleep
import rpyc
import datetime
import dropbox
import os

#from functions import *
class constants:
    
    def __init__(self) :
            self.VideoCaptureIP_ = ""
            self.EV3IP_ = ""
            self.Dropbox_appkey_ = ""
            self.Dropbox_token_ = ""
            self.RPYC_SERVER_PORT = ""
            

            print(" [Start] excute constants.py")

            f = open("gitignore_VideoCaptureIP.txt",'r')
            
            self.VideoCaptureIP_ = f.readline()
            f.close()

            f = open("gitignore_EV3IP.txt",'r')
            self.EV3IP_ = f.readline()
            f.close()

            f = open("gitignore_Dropbox_appkey.txt",'r')
            self.Dropbox_appkey_ = f.readline()
            f.close()

            f = open("gitignore_Dropbox_token.txt",'r')
            self.Dropbox_token_ = f.readline()
            f.close()

            self.RPYC_SERVER_PORT = 18812
            print(" [End] excute constants.py")

