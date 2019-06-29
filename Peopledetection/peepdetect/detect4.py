import cv2
import time
import os
from multiprocessing.pool import ThreadPool

person_cascade = cv2.CascadeClassifier('/home/pi/peepdetect/haarcascade_fullbody.xml')
ub_cascade=cv2.CascadeClassifier('/home/pi/peepdetect/haarcascade_upperbody.xml')
lb_cascade=cv2.CascadeClassifier('/home/pi/peepdetect/haarcascade_lowerbody.xml')
if person_cascade.empty() or ub_cascade.empty() or lb_cascade.empty():
	print('Empty classifier[s]')

def fb(fr):
	#print('Type of passed element:',type(fr))
	#gray_frame = cv2.cvtColor(fr, cv2.COLOR_RGB2GRAY)
	rects = person_cascade.detectMultiScale(fr)
	#print('Type of returned element:',type(rects))
	return rects

def ub(fr):
	rects = ub_cascade.detectMultiScale(fr)
	return rects

def lb(fr):
	rects = lb_cascade.detectMultiScale(fr)
	return rects

pool=ThreadPool(processes=3)
cap = cv2.VideoCapture("1.avi")
while True:
    r, frame = cap.read()
    if r:
        start_time = time.time()
        frame = cv2.resize(frame,(640,360)) # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # Haar-cascade classifier needs a grayscale image
        print("data type of frame:",type(gray_frame))
        #showit(gray_frame)
        rects_r =pool.apply_async(fb,(gray_frame,))
        rects2_r = pool.apply_async(ub,(gray_frame,))
        rects3_r=pool.apply_async(lb,(gray_frame,))
        rects3 = rects3_r.get()
        rects2=rects2_r.get()
        rects=rects_r.get()
        end_time = time.time()
        #print(type(rects))
        print("Elapsed Time:",end_time-start_time)
        print("Number of people=",len(rects)+len(rects2)+len(rects3))
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
        for (x, y, w, h) in rects2:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),2)
        for (x, y, w, h) in rects3:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)
        frame=cv2.resize(frame,(320,180))
        cv2.imshow("preview", frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"): # Exit condition
        break



