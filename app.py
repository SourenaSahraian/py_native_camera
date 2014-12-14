



#!flask/bin/python
from flask import Flask
from numpy import mat
from numpy import random
import time
import threading
import cv2.cv as cv
import video_capture



app = Flask(__name__)


capture = cv.CaptureFromCAM(0)

def my_thread():

    while True:
        video_capture.save_image(cv,5,capture)
        break

    cv.DestroyAllWindows()
    return None


@app.route('/')
def index():
    thread = threading.Thread(target=my_thread)
    thread.start()
    return "Hello"





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=12347, use_reloader=True)


