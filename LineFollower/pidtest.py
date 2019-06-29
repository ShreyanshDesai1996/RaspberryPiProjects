import cv2
import RPi.GPIO as GPIO
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import motors
from simple_pid import PID

#initialisations
camera = PiCamera()
camera.resolution=(320,240)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(0.1)
hthreshold=150 #this will be the sideways threshold
vthreshold=100
bottomthresh=50
flag1=False	#keep turning right while flag 1 is true
flag2=False	#keep turning true while flag2 is true

pid = PID(0.1, 0.1, 0.05, output_limits=(30,70) ,setpoint=0)
pid2 = PID(-0.1, 0.1, 0.05, output_limits=(30,70) ,setpoint=0)

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
    centerx=160
    centery=120
    #print('Area=',area)
    #print('Perimeter=',perim)
    xdiff=centerx-cx
    print('Center x - centroid x',xdiff)
    output1=pid(xdiff)
    output2=pid2((-xdiff))
    print('PID output right=',output1)
    print('PID output left=',output2)
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
	 