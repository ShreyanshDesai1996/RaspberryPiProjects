# import required modules
from flask import Flask, render_template, Response, request
from time import sleep
import RPi.GPIO as GPIO
led=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    #print(request.method)
    if request.method == 'POST':
        if request.form.get('Button1') == 'on':
            print("Turning LED on\n")
            GPIO.output(led,True)
        elif request.form.get('Button1') == 'off':
            print('Turning LED off\n')
            GPIO.output(led,False)
        else:
            # pass # unknown
            print("Unknown Button pressed")
    elif request.method == 'GET':
        print("Get method called")
    return render_template("index.html")


if __name__ == '__main__':
	print('Initialising at main')
	app.run(host='0.0.0.0', debug=False) 
	print('Exiting')

