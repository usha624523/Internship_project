import cv2
import numpy as np
def nothing(x):
    pass
img=cv2.imread('gimg.jpg',1)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
c=0
while(True):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    if c==0:
        print(len(faces))
        c+=1
    for rect in faces:
        (x,y,w,h)=rect
        frame=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
        cv2.imshow('gimg',img)
    key=cv2.waitKey(1)&0xFF
    if key==27:
        break
cv2.destroyAllWindows()

