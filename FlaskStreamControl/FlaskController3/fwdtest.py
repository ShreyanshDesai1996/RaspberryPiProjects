import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
en1=17
in1=24
in2=18
en2=27
in3=22
in4=21

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

pwm1=GPIO.PWM(en1,100)
pwm2=GPIO.PWM(en2,100)
pwm1.start(0)
pwm2.start(0)

GPIO.output(in1, True)
GPIO.output(in2, False)
GPIO.output(in4,True)
GPIO.output(in3,False)

pwm1.ChangeDutyCycle(75)
pwm2.ChangeDutyCycle(75)
GPIO.output(en1,True)
GPIO.output(en2,True)
sleep(1)
GPIO.output(en1,False)
GPIO.output(en2,False)

GPIO.cleanup()
