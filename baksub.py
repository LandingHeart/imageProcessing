import cv2 as cv
import numpy as np 
import sys

cascPath = sys.argv[0]
# cap = cv.VideoCapture('output.avi')
cap = cv.VideoCapture('/videos/walking.mov')
cap.set(3,640) # set Width
cap.set(4,480) # set Height


fgbg = cv.createBackgroundSubtractorMOG2()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    
    fgmask = fgbg.apply(frame)
    cv.imshow('fgmask', fgmask)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()