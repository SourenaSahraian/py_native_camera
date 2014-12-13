#!/usr/bin/python
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2.cv as cv
import video_capture

def run_camera():

    capture = cv.CaptureFromCAM(0)
    while True:
        video_capture.save_image(cv,2,capture)
        break

cv.DestroyAllWindows()

run_camera() # running stand alone