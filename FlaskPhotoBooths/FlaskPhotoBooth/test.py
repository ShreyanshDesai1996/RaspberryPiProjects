# import required modules
from flask import Flask, render_template, Response, request
from picamera import PiCamera
from time import sleep
from flask_bootstrap import Bootstrap

camera = PiCamera()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)



@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Button1') == 'Button1':
            # pass
            capture()
            print("Image Captured")
            return render_template("imshow.html")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")

def before_request():
    app.jinja_env.cache = {}

def capture():
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/FlaskPhotoBooth/static/image.jpg')
    camera.stop_preview()
    return


if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.before_request(before_request)
	print('Initialising at main')
	app.run(host='0.0.0.0', debug=False) 
	print('Exiting')
