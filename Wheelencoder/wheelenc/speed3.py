
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
def init_GPIO():					# initialize GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(sensor1,GPIO.IN,GPIO.PUD_UP)
	GPIO.setup(sensor2,GPIO.IN,GPIO.PUD_UP)

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
	while True:
		calculate_speed()	# call this function with wheel radius as parameter
  		print('pules per second difference in wheels-',diff)
		sleep(0.1)

