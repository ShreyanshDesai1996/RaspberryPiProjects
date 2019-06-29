from RPi import GPIO
from time import sleep

dutycycle=80
counterthresh=293

clk = 17
dt = 18
enable2=21
in3=22
in4=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enable2,GPIO.OUT)

pwm2 = GPIO.PWM(enable2,100)
pwm2.start(0)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
clkLastState = GPIO.input(clk)
dtLastState=GPIO.input(dt)

try:
        GPIO.output(in4,True)
	GPIO.output(in3,False)
	print('Increasing speed 10% duty cycle')
	pwm2.ChangeDutyCycle(dutycycle)

        while abs(counter)<counterthresh:
                clkState = GPIO.input(clk)
                if clkState != clkLastState:
                        dtState = GPIO.input(dt)
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                clkLastState = clkState
	pwm2.ChangeDutyCycle(0)
	print('Final counter= ',counter)

finally:
        GPIO.cleanup()

