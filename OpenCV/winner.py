import cv2
img=cv2.imread('trophy.jpg',1)
print(img)
cv2.imshow('trophy.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
