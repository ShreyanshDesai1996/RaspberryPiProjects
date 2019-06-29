# import required modules
from flask import Flask, render_template, Response, request 
import picamera 
import cv2
import socket 
import io
from forward import movefwd 
app = Flask(__name__) 
vc = cv2.VideoCapture(0) 
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Button1') == 'Button1':
            movefwd()
            print("Button1 pressed")
        elif  request.form.get('Button2') == 'Button2':
            # pass # do something else
            print("Button2 pressed")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        #return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


def gen(): 
   """Video streaming generator function.""" 
   print('Streamer inititalised')
   while True:
        rval, frame = vc.read()
        byteArray = cv2.imencode('t.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + byteArray + b'\r\n')


@app.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 
if __name__ == '__main__': 
	print('Initialising at main')
	app.run(host='0.0.0.0', debug=False, threaded=True) 
	print('Exiting')
