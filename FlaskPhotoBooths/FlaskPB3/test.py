import os
import picamera
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap


camera = picamera.PiCamera()
ctr=0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)

@app.route('/')
def index():
    print('Entered index function')
    hists = os.listdir('static/plots')
    hists = ['plots/' + file for file in hists]
    return render_template('index.html', hists = hists)
    #return render_template('index.html')


@app.route('/takepicture')
def take_picture():
    global ctr
    print('Capturing image number: ',ctr)
    filename='static/plots/'+str(ctr)+'.png'
    camera.capture(filename)
    print('Image saved\n')
    ctr=ctr+1
    return redirect(url_for('index'))


if __name__ == '__main__':
    os.system('rm static/plots/*.*')
    print('Program starting with fresh image dir')
    app.run('0.0.0.0')
