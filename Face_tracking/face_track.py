import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.namedWindow("frame")
cv2.createTrackbar("Neighbours","frame",5,20,nothing)
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    neighbour=cv2.getTrackbarPos("Neighbours","frame")
    faces=face_cascade.detectMultiScale(gray,1.3,neighbour)
    for rect in faces:
        (x,y,w,h)=rect
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        cv2.imshow('frame',frame)
    key=cv2.waitKey(1)&0xFF
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()

