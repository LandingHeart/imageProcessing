import cv2 as cv
import numpy as np 
import sys

cascPath = sys.argv[0]
cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
face_cascade = cv.CascadeClassifier('/Users/shinan/Desktop/imageProcessing/data/haarcascades/haarcascade_frontalface_default.xml')


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    font = cv.FONT_HERSHEY_SIMPLEX



    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame,'Me',(x - 50, y + 180), font, 2, (200,80,155), 2, cv.LINE_AA)

    # Display the resulting frame
    cv.imshow('Video', frame)
    cv.imshow('Video2', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv.destroyAllWindows()