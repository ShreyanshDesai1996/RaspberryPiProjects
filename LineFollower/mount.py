import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
panpin=26
tiltpin=19

GPIO.setup(panpin,GPIO.OUT)
pwmpan=GPIO.PWM(panpin,50)
GPIO.setup(tiltpin,GPIO.OUT)
pwmtilt=GPIO.PWM(tiltpin,50)

def setpan(angle):
    duty=angle/18+2
    pwmpan.start(duty)
    time.sleep(0.5)
    pwmpan.stop()
    
def settilt(angle):
    duty=angle/18+2
    pwmtilt.start(duty)
    time.sleep(0.5)
    pwmtilt.stop()
    
