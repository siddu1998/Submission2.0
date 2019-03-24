import cv2
img=cv2.imread('00131.jpeg')
Y,X,_=img.shape
horizontal_line_start,horizontal_line_end =(0,Y/2),(X,Y/2)
vertical_line_start,vertical_line_end =(X/2,0),(X/2,Y)
cv2.circle(img,(X/2,Y/2),5,(255,0,0),2)
cv2.line(img,vertical_line_start,vertical_line_end,(0,255,255),4)
cv2.line(img,horizontal_line_start,horizontal_line_end,(0,255,255),4)
cv2.imshow('new',img)
cv2.waitKey(0) 
