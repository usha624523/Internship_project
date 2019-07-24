import cv2
img=cv2.imread('pic.jpg',-1)
print(img)
cv2.imshow('pic.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
