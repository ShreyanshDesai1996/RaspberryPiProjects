from RPi import GPIO
from time import sleep

clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
clkLastState = GPIO.input(clk)
dtLastState=GPIO.input(dt)
try:
        while True:
                clkState = GPIO.input(clk)
                dtState=GPIO.input(dt)
                if(clkState!=clkLastState or dtState!=dtLastState):
                    #print('c2= ',dtState)
                    print('c1= ',clkState)
                    print('c2= ',dtState)
                    print()
                    #sleep(0.01)
                    clkLastState=clkState
                    dtLastState=dtState
finally:
        GPIO.cleanup()
