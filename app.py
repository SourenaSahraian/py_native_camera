#!flask/bin/python
from flask import Flask
from numpy import mat
from numpy import random
import time
import threading
import TestCamera
from multiprocessing import Process

app = Flask(__name__)


def my_thread():
    time.sleep(2)
    TestCamera.run_camera()
    return None


@app.route('/')
def index():
    thread = threading.Thread(target=my_thread)
    thread.start()
    # p = Process(target=my_thread())
    #p.start()
    #p.join()
    return "Hello man !"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=12346, use_reloader=True) # run this on a differen port as sockets keep geting clogged