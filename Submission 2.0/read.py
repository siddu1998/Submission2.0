import cv2
img=cv2.imread('road_marked.jpg')
img=cv2.resize(img,(1000,1000))
cv2.imshow('img',img)
cv2.waitKey(0)