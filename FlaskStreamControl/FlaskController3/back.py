import RPi.GPIO as GPIO
from time import sleep
def moveback():
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

	GPIO.output(in1,False)
	GPIO.output(in2,True)
	GPIO.output(in4,False)
	GPIO.output(in3,True)
	print('Moving forward')
	#GPIO.output(enable1,GPIO.HIGH)
	#GPIO.output(enable2,GPIO.HIGH)
	print('Increasing speed 100% duty cycle')
	pwm1.ChangeDutyCycle(100)
	pwm2.ChangeDutyCycle(100)
	sleep(1)
	print('Stopping,performing cleanup')
	#GPIO.output(enable1,GPIO.LOW)
	#GPIO.output(enable2,GPIO.LOW)

	GPIO.cleanup()


