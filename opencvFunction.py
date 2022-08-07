

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

class WebCamCV :
    
    def __init__(self,VideoCaptureIP_ ) -> None:
        self.VideoCaptureIP_ = VideoCaptureIP_
        
        
        