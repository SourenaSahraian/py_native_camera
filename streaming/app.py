__author__ = 'soorenasahraian'
from flask import Flask, render_template, Response

# emulated camera
from camera import Camera
import cv2.cv as cv
import cv2
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


camera=cv2.VideoCapture(0)
Camera.camera=camera
print("once")

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + (frame) + b'\r\n')


@app.route('/feeds')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera(camera)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#camera.release()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)