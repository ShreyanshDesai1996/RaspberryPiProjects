
import RPi.GPIO as GPIO
from time import sleep
import time, math

pps1 = 0
elapse1= 0
sensor1= 23
pulse1= 0
start_timer1 = time.time()
start_timer2=time.time()
pulse2=0
sensor2=25
elapse2=0
pps2=0
diff=0

enable1=24
enable2=21
in3=22
in2=18
in4=27
in1=17


def init_GPIO():					# initialize GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(sensor1,GPIO.IN,GPIO.PUD_UP)
	GPIO.setup(sensor2,GPIO.IN,GPIO.PUD_UP)
	GPIO.setup(enable1,GPIO.OUT)
	GPIO.setup(enable2,GPIO.OUT)
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)
	GPIO.setup(in3,GPIO.OUT)
	GPIO.setup(in4,GPIO.OUT)
	


def calculate_elapse1(channel):				# callback function
	global pulse1, start_timer1, elapse1
	pulse1+=1								# increase pulse by 1 whenever interrupt occurred
	elapse1 = time.time() - start_timer1
	#adding below line shd		# elapse for every 1 complete rotation made!
	#pulse=0
	start_timer1 = time.time()				# let current time equals to start_timer

def calculate_elapse2(channel):
	global pulse2, start_timer2,elapse2
	pulse2+=1
	elapse2=time.time()-start_timer2
	start_timer2=time.time()

def calculate_speed():
	global pps1,elapse1,pps2,elapse2,diff
	if elapse1 !=0 and elapse2!=0:							# to avoid DivisionByZero error
		pps1 = 1/elapse1
		pps2 = 1/elapse2
		diff=pps1-pps2
		return diff

def init_interrupt():
	GPIO.add_event_detect(sensor1, GPIO.FALLING, callback = calculate_elapse1, bouncetime = 1)
	GPIO.add_event_detect(sensor2, GPIO.FALLING, callback = calculate_elapse2,bouncetime=1)

if __name__ == '__main__':
	init_GPIO()
	init_interrupt()

	sensitivity=40

	pwm1=GPIO.PWM(enable1,100)
	pwm2=GPIO.PWM(enable2,100)
	pwm1.start(0)
	pwm2.start(0)
	GPIO.output(in4,True)
	GPIO.output(in3,False)
	GPIO.output(in2,False)
	GPIO.output(in1,True)
	currDuty1=30
	currDuty2=30
	newDuty1=30
	newDuty2=30
	pwm1.ChangeDutyCycle(currDuty1)
	pwm2.ChangeDutyCycle(currDuty2)
	while True:
		calculate_speed()	# call this function with wheel radius as parameter
  		print('pules per second difference in wheels-',diff)
		if(diff>sensitivity): #if pps1>pps2
			print('Detected wheel 1 faster than 2, increasing speed of 2')
			currDuty2=currDuty2+2
			pwm2.ChangeDutyCycle(currDuty2)
		if(diff<(-sensitivity)): #if pps1<pps2
			print('Detected wheel 2 faster than 1, increasing speed of 1')
			currDuty1=currDuty1+2
			pwm2.ChangeDutyCycle(currDuty1)
		sleep(0.1)


GPIO.cleanup()
