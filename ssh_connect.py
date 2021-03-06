import paramiko
import getpass

from constants import *


class ssh_connect :
    
    def __init__(self , EV3IP_):
        print(__name__)
        print(" [Start] ssh connect to EV3 , ssh_connect.py")
        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        
        server = EV3IP_ #= input("Server: ")  # 호스트명이나 IP 주소
        user = 'robot'  #= input("Username: ")  
        pwd = 'maker'   #= getpass.getpass("Password: ") # 암호입력 숨김

        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        
        cli.connect(EV3IP_, port = 22,  username=user, password=pwd)
        stdin, stdout, stderr = cli.exec_command("python3 /usr/local/bin/rpyc_classic.py -m threaded --host 0.0.0.0")
        #lines = stdout.readlines()
        #print(''.join(lines))
        
        cli.close()

        print(" [End] ssh connect to EV3 , ssh_connect.py")


