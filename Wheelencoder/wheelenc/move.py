import RPi.GPIO as GPIO
from time import sleep
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

try:
	while True:
		GPIO.output(in4,True)
		GPIO.output(in3,False)
		GPIO.output(in2,False)
		GPIO.output(in1,True)
		print('Increasing speed 35% duty cycle')
		pwm1.ChangeDutyCycle(35)
		pwm2.ChangeDutyCycle(35)
		sleep(5)
		print('Changing to 25% duty cycle')
		pwm1.ChangeDutyCycle(25)
		pwm2.ChangeDutyCycle(25)
		sleep(5)
		print('Changing to 30% duty cycle')
		pwm1.ChangeDutyCycle(30)
		pwm2.ChangeDutyCycle(30)
		sleep(5)
		print('Changing to 35% duty cycle')
		pwm1.ChangeDutyCycle(35)
		pwm2.ChangeDutyCycle(35)
		sleep(5)
		break

	GPIO.cleanup()
except KeyboardInterrupt:
	print('Stopping cleanly')
	GPIO.cleanup()
