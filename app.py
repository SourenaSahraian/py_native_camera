



#!flask/bin/python
from flask import Flask,send_file
from numpy import mat
from numpy import random
import time
import threading
import cv2.cv as cv
import cv2
import video_capture
import Queue
from flask import Flask, render_template, Response

app = Flask(__name__)


capture = cv.CaptureFromCAM(0)


app = Flask(__name__)

#http://127.0.0.1:12349/feed


@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        frame = cv.QueryFrame(capture)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + send_file(frame) + b'\r\n')

@app.route('/feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=12349, use_reloader=True)



