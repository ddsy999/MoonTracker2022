
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
def constants():
    
    global VideoCaptureIP_ 
    global EV3IP_ 
    global Dropbox_appkey_ 
    global Dropbox_token_ 
    global RPYC_SERVER_PORT
    
    print(" [Start] excute constants.py")

    f = open("gitignore_VideoCaptureIP.txt",'r')
    
    VideoCaptureIP_ = f.readline()
    f.close()

    f = open("gitignore_EV3IP.txt",'r')
    EV3IP_ = f.readline()
    f.close()

    f = open("gitignore_Dropbox_appkey.txt",'r')
    Dropbox_appkey_ = f.readline()
    f.close()

    f = open("gitignore_Dropbox_token.txt",'r')
    Dropbox_token_ = f.readline()
    f.close()

    RPYC_SERVER_PORT = 18812
    print(" [End] excute constants.py")

constants()