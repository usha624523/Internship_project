import random
import cv2
lst=['rock','paper','scissor']
player1=input("enter:")
player2=input("enter:")
print('player1:{0}'.format(player1))
print('player2:{0}'.format(player2))
if(player1==player2):
    print("tie")
elif(player1=='rock' and player2=='paper'):
    print('player1 losses')
    img1=cv2.imread('loose.jpg',1)
    print(img1)
    cv2.imshow('loose.jpg',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif(player1=='rock' and player2=='scissor'):
    print('player1 wins')
    img=cv2.imread('trophy.jpg',1)
    print(img)
    cv2.imshow('trophy.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif(player1=='paper' and player2=='scissor'):
    print('player1 losses')
    img1=cv2.imread('loose.jpg',1)
    print(img1)
    cv2.imshow('loose.jpg',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif(player1=='paper' and player2=='rock'):
    print('player1 wins')
    img=cv2.imread('trophy.jpg',1)
    print(img)
    cv2.imshow('trophy.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif(player1=='scissor' and player2=='paper'):
    print('player1 wins')
    img=cv2.imread('trophy.jpg',1)
    print(img)
    cv2.imshow('trophy.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('player1 losses')
    img1=cv2.imread('loose.jpg',1)
    print(img1)
    cv2.imshow('loose.jpg',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
