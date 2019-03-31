import cv2 as cv
import numpy as np 
import sys
cap = cv.VideoCapture('output.avi')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
 
    cv.imshow('original',frame)
    cv.imshow('frame',fgmask)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
        
cap.release()
cv.destroyAllWindows()