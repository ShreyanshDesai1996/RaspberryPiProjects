import RPi.GPIO as GPIO
import time
#motor contoller pin definitions
enable1=24
enable2=21
in3=22
in2=18
in4=27
in1=17
GPIO.setmode(GPIO.BCM)
#motor contoller begin
GPIO.setup(enable1,GPIO.OUT)
GPIO.setup(enable2,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
pwm1 = GPIO.PWM(enable1,100)    # Created a PWM object
pwm2 = GPIO.PWM(enable2,100)
pwm1.start(0) #right wheel
pwm2.start(0) #left wheel
GPIO.output(in1,True)
GPIO.output(in2,False)
GPIO.output(in3,False)
GPIO.output(in4,True)

#setting duty cycles for straight and turns
basedc=30
turningdc=50

def initialiser():
	pwm1.ChangeDutyCycle(basedc)
	pwm2.ChangeDutyCycle(basedc)
	
	
def turn_right():
	GPIO.output(in1,False)
	GPIO.output(in2,True)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	pwm1.ChangeDutyCycle(turningdc)
	pwm2.ChangeDutyCycle(turningdc)
	
def turn_left():
	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,True)
	GPIO.output(in4, False)
	pwm1.ChangeDutyCycle(turningdc)
	pwm2.ChangeDutyCycle(turningdc)
	
	
def stop():
	print('Stop, ending loop')
	pwm1.ChangeDutyCycle(0)
	pwm2.ChangeDutyCycle(0)
	time.sleep(3)

def straight():
	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	pwm1.ChangeDutyCycle(basedc)
	pwm2.ChangeDutyCycle(basedc)

def joint_left():
	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	pwm1.ChangeDutyCycle(basedc)
	pwm2.ChangeDutyCycle(basedc)
	time.sleep(0.55)
	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,True)
	GPIO.output(in4, False)
	pwm1.ChangeDutyCycle(turningdc)
	pwm2.ChangeDutyCycle(turningdc)
	time.sleep(1)

def joint_right():
	GPIO.output(in1,True)
	GPIO.output(in2,False)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	pwm1.ChangeDutyCycle(basedc)
	pwm2.ChangeDutyCycle(basedc)
	time.sleep(0.55)
	GPIO.output(in1,False)
	GPIO.output(in2,True)
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	pwm1.ChangeDutyCycle(turningdc)
	pwm2.ChangeDutyCycle(turningdc)
	time.sleep(1)
