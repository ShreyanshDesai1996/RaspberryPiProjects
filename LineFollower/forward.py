import RPi.GPIO as GPIO
from time import sleep
def movefwd():
	GPIO.setmode(GPIO.BCM)
	enable1=24
	enable2=21
	in3=22
	in2=18
	in4=27
	in1=17
	GPIO.setup(enable1,GPIO.OUT)
	GPIO.setup(enable2,GPIO.OUT)
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)
	GPIO.setup(in3,GPIO.OUT)
	GPIO.setup(in4,GPIO.OUT)
	pwm1 = GPIO.PWM(enable1,100)    # Created a PWM object
	pwm2 = GPIO.PWM(enable2,100)
	pwm1.start(0)
	pwm2.start(0)

	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in4,True)
	GPIO.output(in3,False)
	print('Moving forward')
	#GPIO.output(enable1,GPIO.HIGH)
	#GPIO.output(enable2,GPIO.HIGH)
	dc=40
	print('Increasing speed,  duty cycle=',dc)
	pwm1.ChangeDutyCycle(dc)
	pwm2.ChangeDutyCycle(dc)
	sleep(2)
	print('Stopping,performing cleanup')
	#GPIO.output(enable1,GPIO.LOW)
	#GPIO.output(enable2,GPIO.LOW)

	GPIO.cleanup()


movefwd()
