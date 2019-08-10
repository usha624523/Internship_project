import cv2
import numpy as np
def f():
    #empty function
 cv2.createButton('Button',f)

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read();
    blurred_frame=cv2.GaussianBlur(frame,(3,3),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    
    lower_blue=np.array([38,86,0])
    upper_blue=np.array([121,255,255])
    lower_red=np.array([0,100,100])
    upper_red=np.array([10,255,255])
    lower_green=np.array([36,25,25])
    upper_green=np.array([70,255,255])
    
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    mask2=cv2.inRange(hsv,lower_green,upper_green)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    result=cv2.bitwise_and(frame,frame,mask=mask1+mask+mask2)
    #result=cv2.bitwise_and(frame,frame,mask=mask)
    
    for contour in contours:
        area=cv2.contourArea(contour)

        if area>100:
            cv2.drawContours(frame,contours,-1,(0,255,0),3)
            cv2.drawContours(frame,contours,-1,(0,0,255),3)
            cv2.drawContours(frame,contours,-1,(0,0,255),3)
    cv2.imshow('frame',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Mask',mask1)
    cv2.imshow('Mask',mask2)
    cv2.imshow('Result',result)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
