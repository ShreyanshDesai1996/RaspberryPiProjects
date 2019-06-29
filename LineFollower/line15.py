import cv2
import RPi.GPIO as GPIO
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from simple_pid import PID
import mount #for camera mount
import ultra #for distance sensor

mount.setpan(90)
mount.settilt(120)

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
pwm1.start(40) #right wheel
pwm2.start(40) #left wheel
GPIO.output(in1,True)
GPIO.output(in2,False)
GPIO.output(in3,False)
GPIO.output(in4,True)


#initialisations
camera = PiCamera()
camera.resolution=(320,240)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)



initialised = False

turnlist=["left"]
turnum=0

#to check if prev state was straight
#prevstraight=True

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image=frame.array
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)#blur the grayscale image
    ret,th1 = cv2.threshold(blur,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#using threshold remave noise
    ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
    contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)	#choose the largest contour
    M=cv2.moments(c)
    
    cx=int(M["m10"]/M["m00"])
    cy=int(M["m01"]/M["m00"])
    
    #perform correction
    #can add more elifs to turn right/left slowly,fast
    
    centerx=160
    #print('Area=',area)
    #print('Perimeter=',perim)
    xdiff=centerx-cx
    dist=ultra.distance()
    
    
    while(dist<7):
        print('Obstruction detected,stop')
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        time.sleep(0.5)
        dist=ultra.distance()
    
    
    if(abs(xdiff)<50):
        print('Center x - centroid x',xdiff)
        GPIO.output(in1,True)
        GPIO.output(in2,False)
        GPIO.output(in3,False)
        GPIO.output(in4,True)
        pwm1.ChangeDutyCycle(30)
        pwm2.ChangeDutyCycle(30)
        #time.sleep(0.5)
    
    else:
        pid = PID(0.8, 0.2, 0.05, output_limits=(-50,50) ,setpoint=0)
        pid2 = PID(0.8, 0.2, 0.05, output_limits=(-50,50) ,setpoint=0)
        #pid.auto_mode = True
        #pid2.auto_mode = True
        output1=pid(xdiff)
        output2=pid2((-xdiff))
        if(output1<0):
            GPIO.output(in1,False)
            GPIO.output(in2,True)
        if(output1>=0):
            GPIO.output(in1,True)
            GPIO.output(in2,False)
        if(output2<0):
            GPIO.output(in3,True)
            GPIO.output(in4,False)
        if(output2>=0):
            GPIO.output(in3,False)
            GPIO.output(in4,True)
        print('PID output right=',output1)
        print('PID output left=',output2)
        pwm1.ChangeDutyCycle(abs(output1))
        pwm2.ChangeDutyCycle(abs(output2))
    
    cv2.drawContours(image,c,-1,(0,255,0),3)
    cv2.circle(image,(cx,cy),7,(255,255,255),-1)
    cv2.circle(image,(160,120),7,(255,255,255),-1)
    cv2.line(image,(160,120),(cx,cy),(255,0,0),5)
    

    cv2.imshow('frame',image) #show video
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    rawCapture.truncate(0)


cv2.destroyAllWindows()


