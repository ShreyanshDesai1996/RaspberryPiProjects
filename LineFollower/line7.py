import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution=(640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

hthreshold=100 #this will be the sideways threshold
              #if centroid crosses it on either side of the center(320) it will do a correction
vthreshold=50
flag1=False	#keep turning right while flag 1 is true
flag2=False	#keep turning true while flag2 is true


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
    if ((cx<320-hthreshold and cy<240+vthreshold) or flag1) : #turn right
          #keep turning till centered
        if(cx<320):
            flag1=True
        elif(cx>320 and cx<320+hthreshold):
            flag1=False
        print('Right')
    elif((cx>320+hthreshold and cy<240+vthreshold) or flag2): #turn left
        if(cx>320):
            flag2=True
        elif(cx<320 and cx>320-hthreshold):
            flag2=False
        print('Left')
    else:
        flag1=False;
        flag2=False;
        print('Straight')
    cv2.drawContours(image,c,-1,(0,255,0),3)
    cv2.line(image,(0,240+vthreshold),(640,240+vthreshold),2)
    cv2.line(image,(320,0),(320,480),(255,0,0),5) #center line
    cv2.line(image,(320-hthreshold,0),(320-hthreshold,480),(0,0,255),2) #left threshold
    cv2.line(image,(320+hthreshold,0),(320+hthreshold,480),(0,0,255),2) #right threshold
    cv2.circle(image,(cx,cy),7,(255,255,255),-1) #centroid
    image=cv2.resize(image,(320,240))

    cv2.imshow('frame',image) #show video
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    rawCapture.truncate(0)


cv2.destroyAllWindows()

