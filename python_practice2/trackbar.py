import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")
cv2.createTrackbar('L_H','Trackbar',0,179,nothing)#HSV=Hue Saturation Value
cv2.createTrackbar('L_S','Trackbar',0,255,nothing)
cv2.createTrackbar('L_V','Trackbar',0,255,nothing)
cv2.createTrackbar('U_H','Trackbar',179,179,nothing)
cv2.createTrackbar('U_S','Trackbar',255,255,nothing)
cv2.createTrackbar('U_V','Trackbar',255,255,nothing)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2XYZ)
    l_h=cv2.getTrackbarPos('L_H','Trackbar')
    l_s=cv2.getTrackbarPos('L_S','Trackbar')
    l_v=cv2.getTrackbarPos('L_V','Trackbar')
    u_h=cv2.getTrackbarPos('U_H','Trackbar')
    u_s=cv2.getTrackbarPos('U_S','Trackbar')
    u_v=cv2.getTrackbarPos('U_V','Trackbar')

    lower=np.array([l_h,l_s,l_v])
    upper=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,lower,upper)

    result=cv2.bitwise_and(frame,frame,mask=mask)
                
    cv2.imshow('Frame',hsv)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',result)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

