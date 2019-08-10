import cv2
import numpy as np
from tkinter import *
def nothing(x):
    pass

root = Tk()               
cap=cv2.VideoCapture(0)
root.geometry('100x100')
btn = Button(root, text = 'blue !', bd = '5',command = root.destroy)      
btn.pack(side = 'top')      
btn1 = Button(root, text = 'red !', bd = '5',command = root.destroy)      
btn1.pack(side = 'left')      

root.mainloop()
while True:
    _, frame=cap.read()
    blurred_frame=cv2.GaussianBlur(frame,(1,1),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    cv2.createTrackbar("neighbour","Frame",0,254,nothing)
    Neighbours=cv2.getTrackbarPos("1","Frame")
    if btn:
        lower_b=np.array([38,86,0])
        upper_b=np.array([121,255,255])
        mask=cv2.inRange(hsv,lower_b,upper_b)
    if btn1:
        lower_b=np.array([0,100,100])
        upper_b=np.array([10,255,255])
        mask=cv2.inRange(hsv,lower_b,upper_b)
    contours, _=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area=cv2.contourArea(contour)
        cv2.drawContours(frame,contour,-1,(0,255,0),3)
    
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
   
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
