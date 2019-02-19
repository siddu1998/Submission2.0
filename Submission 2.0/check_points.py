import cv2

img=cv2.imread('00130.jpeg')
cv2.circle(img,(614,443),3,(0,244,33),1)
cv2.imshow('point',img)
cv2.waitKey(0)