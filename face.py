import cv2 as cv
import numpy as np 
import sys

cascPath = sys.argv[0]
face_cascade = cv.CascadeClassifier('/Users/shinan/Desktop/imageProcessing/data/haarcascades/haarcascade_frontalface_default.xml')
video_capture = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

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

    # Display the resulting frame
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv.destroyAllWindows()