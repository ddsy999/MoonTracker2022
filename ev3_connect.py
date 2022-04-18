

def ev3_connect():
    import rpyc
    
    global conn
    global ev3
    global m_updown
    global m_leftright
    global ev3_screen
    global ev3_sound
    global ev3connect
    
    print(" [Start] EV3 rpyc connect , ev3_connect.py")

    # EV3

    # ev3connect
    # 0 is not conn / 1 is conn
    try:
        conn = rpyc.classic.connect( EV3IP_ , port=RPYC_SERVER_PORT)
        ev3 = conn.modules['ev3dev.ev3'] # import ev3dev.ev3 remotely
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

