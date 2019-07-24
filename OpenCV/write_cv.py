import cv2
img=cv2.imread('loose.jpg')
print(img)
cv2.imshow('loose',img)
k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('loose_copy.jpg',img)
    cv2.destroyAllWindows()
    
