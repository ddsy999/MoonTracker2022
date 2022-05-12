
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
from importlib import reload




from constants import *
from ssh_connect import *


cons = constants()


ssh_conn = ssh_connect(cons.EV3IP_)



try:
    connEV3 = rpyc.classic.connect( cons.EV3IP_ , port=cons.RPYC_SERVER_PORT)
    ev3 = connEV3.modules['ev3dev.ev3'] # import ev3dev.ev3 remotely
    m_updown = ev3.LargeMotor('outA')
    m_leftright = ev3.Motor('outB')
    ev3_screen = ev3.Screen()
    ev3_screen.draw.text((30,30),"Connect")
    ev3_screen.update()


    ev3_sound = ev3.Sound()
    ev3_sound.beep()

    ev3connect = 1
    
    print(" [End] EV3 rpyc connect , ev3_connect.py")
    
except:
    print(" [Err] EV3 rpyc connect , ev3_connect.py")
    ev3connect = 0



m_updown.run_timed(speed_sp=-100, time_sp=500)