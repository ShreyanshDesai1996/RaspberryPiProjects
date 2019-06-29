import os
import picamera
from flask import Flask, render_template, redirect, url_for, Response, request
from flask_bootstrap import Bootstrap
import io
import socket
import cv2

vc=cv2.VideoCapture(0)
ctr=0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)

@app.route('/')
def index():
    print('Entered index function')
    hists = os.listdir('static')
    hists = [file for file in hists]
    return render_template('index.html', hists = hists)
    #return render_template('index.html')


@app.route('/takepicture')
def take_picture():
    global ctr
    print('Capturing image number: ',ctr)
    filename='static/'+str(ctr)+'.png'
    rval,frame = vc.read()
    cv2.imwrite(filename,frame)
    print('Image saved\n')
    ctr=ctr+1
    return redirect(url_for('index'))
    

def gen(): 
   """Video streaming generator function.""" 
   print('Streamer inititalised')
   while True:
        rval, frame = vc.read()
        byteArray = cv2.imencode('t.jpg', cv2.flip(frame,-1))[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + byteArray + b'\r\n')


@app.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 


if __name__ == '__main__':
    os.system('rm static/*.*')
    print('Program starting with fresh image dir')
    app.run('0.0.0.0')
