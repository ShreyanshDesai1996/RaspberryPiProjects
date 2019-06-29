import RPi.GPIO as GPIO
import time
def detecte(channel):
	print('Event detected')


GPIO.setmode(GPIO.BCM)
bpin=17
GPIO.setup(bpin,GPIO.IN) #,pull_up_down=GPIO.PUD_DOWN)
try:
		GPIO.add_event_detect(bpin, GPIO.RISING, callback=detecte, bouncetime=100)
		while True:
			print('Running')
			time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()

finally:
	GPIO.cleanup()
