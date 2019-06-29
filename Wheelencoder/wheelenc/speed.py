
import RPi.GPIO as GPIO
from time import sleep
import time, math

pps = 0
elapse= 0
sensor= 23
pulse= 0
start_timer = time.time()

def init_GPIO():					# initialize GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(sensor,GPIO.IN,GPIO.PUD_UP)

def calculate_elapse(channel):				# callback function
	global pulse, start_timer, elapse
	pulse+=1								# increase pulse by 1 whenever interrupt occurred
	elapse = time.time() - start_timer
	#adding below line shd		# elapse for every 1 complete rotation made!
	#pulse=0
	start_timer = time.time()				# let current time equals to start_timer

def calculate_speed():
	global pps,elapse
	if elapse !=0:							# to avoid DivisionByZero error
		pps = 1/elapse
		return pps

def init_interrupt():
	GPIO.add_event_detect(sensor, GPIO.FALLING, callback = calculate_elapse, bouncetime = 1)

if __name__ == '__main__':
	init_GPIO()
	init_interrupt()
	while True:
		calculate_speed()	# call this function with wheel radius as parameter
  		print('pules per second-',pps)
		sleep(0.1)
