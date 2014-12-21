__author__ = 'soorenasahraian'

import time
import cv2.cv as cv
import threading
import cv2
import os
import numpy as np
import Queue
import io
import StringIO
from PIL import Image

#cam = cv.CaptureFromCAM(0)


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    camera=None



    def __init__(self,cam):
        if self.thread is None:
            self.camera=cam
            # start background frame thread
            self.thread = threading.Thread(target=self._thread)
            self.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(1)

    def get_frame(self):
        return self.frame

    @classmethod
    def _thread(cls):
          while True:
                # store frame


            _,cv2_im = cls.camera.read()
            #cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2GRAY)
            #cls.camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,320);
           # cls.camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,320);
            cv2.imwrite("test.jpeg", cv2_im)
            time.sleep(1)
            pil_im=im = Image.open("test.jpeg")
            if pil_im is None:
                time.sleep(1)
            #pil_im.draft("L", (300, 300))
           # area=(300,300,600,900)
            #pil_im=pil_im.crop(area)
            output = StringIO.StringIO()
            pil_im.save(output,format="jpeg")
            contents = output.getvalue()
            cls.frame=contents



    #cap.release()
    #cv2.destroyAllWindows()