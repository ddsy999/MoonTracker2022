

class ev3_connect :
    import rpyc
    global  conn       
    global  ev3        
    global  m_updown   
    global  m_leftright
    global  ev3_screen 
    global  ev3_sound  
    global  ev3connect 

    
    def __init__(self,EV3IP_,RPYC_SERVER_PORT) -> None:
        
        import paramiko
        import rpyc
        self.EV3IP_     = EV3IP_
        self.RPYC_SERVER_PORT = RPYC_SERVER_PORT
        self.conn       = "none"
        self.ev3        = "none"
        self.m_updown   = "none"
        self.m_leftright= "none"
        self.ev3_screen = "none"
        self.ev3_sound  = "none"
        self.ev3connect = 0 
        
        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        server = EV3IP_ #= input("Server: ")  # 호스트명이나 IP 주소
        user = 'robot'  #= input("Username: ")  
        pwd = 'maker'   #= getpass.getpass("Password: ") # 암호입력 숨김

        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        
        cli.connect(self.EV3IP_, port = 22,  username=user, password=pwd)
        stdin, stdout, stderr = cli.exec_command("python3 /usr/local/bin/rpyc_classic.py -m threaded --host 0.0.0.0")
        # lines = stdout.readlines()
        # print(''.join(lines))
        
        cli.close()

    

        print(" [Start] EV3 rpyc connect , ev3_connect.py")

        # EV3

        # ev3connect
        # 0 is not conn / 1 is conn
        try:
            self.conn = rpyc.classic.connect( self.EV3IP_ , port = self.RPYC_SERVER_PORT)
            self.ev3 = self.conn.modules['ev3dev.ev3'] # import ev3dev.ev3 remotely
            self.m_leftright = self.ev3.Motor('outA')
            self.m_updown = self.ev3.LargeMotor('outB')
            
            self.ev3_screen = self.ev3.Screen()
            self.ev3_screen.draw.text((30,30),"Connect")
            self.ev3_screen.update()


            self.ev3_sound = self.ev3.Sound()
            self.ev3_sound.beep()

            self.ev3connect = 1
            
            conn        = self.conn       
            ev3         = self.ev3        
            m_updown    = self.m_updown   
            m_leftright = self.m_leftright
            ev3_screen  = self.ev3_screen 
            ev3_sound   = self.ev3_sound  
            ev3connect  = self.ev3connect 

            print(" [End] success")

        except:
            print(" [Err] ")
            self.ev3connect = 0


    def MotorLR(self , speed_ , time_):
        self.m_leftright.run_timed(speed_sp=speed_, time_sp=time_)
        
    def MotorUD(self , speed_ , time_):
        self.m_updown.run_timed(speed_sp=speed_, time_sp=time_)    
