import RPi.GPIO as GPIO
from time import sleep
def movefwd():
	GPIO.setmode(GPIO.BCM)
	enable1=17
	enable2=27
	in3=22
	in2=18
	in4=21
	in1=24
	GPIO.setup(enable1,GPIO.OUT)
	GPIO.setup(enable2,GPIO.OUT)
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)
	GPIO.setup(in3,GPIO.OUT)
	GPIO.setup(in4,GPIO.OUT)
	pwm1 = GPIO.PWM(in1,100)    # Created a PWM object
	pwm2 = GPIO.PWM(in4,100)
	pwm1.start(0)
	pwm2.start(0)

	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	print('Moving forward')
	GPIO.output(enable1,GPIO.HIGH)
	GPIO.output(enable2,GPIO.HIGH)
	print('Increasing speed 100% duty cycle')
	pwm1.ChangeDutyCycle(75)
	pwm2.ChangeDutyCycle(75)
	sleep(1)
	print('Stopping,performing cleanup')
	GPIO.output(enable1,GPIO.LOW)
	GPIO.output(enable2,GPIO.LOW)

	GPIO.cleanup()

