import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()#to capture frame by frame
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',hsv)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
