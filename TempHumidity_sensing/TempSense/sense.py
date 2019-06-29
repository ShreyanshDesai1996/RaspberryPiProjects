#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)
fan_pin=17
GPIO.setup(fan_pin,GPIO.OUT,initial=GPIO.LOW)
prev_state='off'
temp_thresh=32.0

try:
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print(type(temperature),temperature)
        print(temperature>=temp_thresh)
        if(temperature>=temp_thresh and prev_state=='off'):
            GPIO.output(fan_pin,True)
            GPIO.output(fan_pin,GPIO.HIGH)
            pre_state='on'
        elif(temperature<temp_thresh and prev_state=='on'):
            GPIO.output(fan_pin,False)
            prev_state='off'
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        time.sleep(2)

except KeyboardInterrupt:
    print('Exiting')
    GPIO.cleanup()
