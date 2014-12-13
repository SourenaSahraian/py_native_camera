__author__ = 'soorenasahraian'
import time
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2.cv as cv
def save_image(cv,number_of_shots,capture):
    for i in range(0,number_of_shots):
         img = cv.QueryFrame(capture)
         cv.SaveImage(str(i)+".jpeg", img) # actually save the image
         time.sleep(1)
    return False
