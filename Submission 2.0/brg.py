import cv2
image=cv2.imread('0002879.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image-gray',gray)
cv2.waitKey(0)