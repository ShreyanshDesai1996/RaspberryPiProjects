import RPi.GPIO as GPIO
from time import sleep
def movefwd():
	GPIO.setmode(GPIO.BCM)
	enable=17
	motor1=21

	GPIO.setup(enable,GPIO.OUT)
	GPIO.setup(motor1,GPIO.OUT)
	pwm = GPIO.PWM(motor1, 100)    # Created a PWM object

	pwm.start(0)
	print('Moving forward')
	GPIO.output(enable,GPIO.HIGH)
	print('Increasing speed 25% duty cycle')
	pwm.ChangeDutyCycle(25)
	sleep(1)
	print('Increasing speed 50% duty cycle')
	pwm.ChangeDutyCycle(50)
	sleep(1)
	print('Max speed 100% duty cycle')
	pwm.ChangeDutyCycle(100)
	sleep(1)

	print('Stopping,performing cleanup')
	GPIO.output(enable,GPIO.LOW)

	GPIO.cleanup()
