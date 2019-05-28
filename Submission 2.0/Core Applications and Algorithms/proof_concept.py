"""
Sai Siddartha Maram | Esther Ling
Initial Proof of concept : 
1. take in input image 
2. Plot points on the road 
3. get bird view
4. approximate dimentsions
"""

#cv2 python image processing library
import cv2
#numpy for image slicing and spliting images which are big
import numpy as np



"""
def draw_circle(event,mouse_x,mouse_y,flag,param):
    if event is double click the keypad draw a circle
"""
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img2,(x,y),10,(255,0,0),-1)


#load image from file system
img = cv2.imread('0018705.jpg')
#get height and width of the image
h,w,_=img.shape
#create a clone named img2
img2=img[int(h/2):h,0:w]
cv2.namedWindow('image')
#and do the painiting on image2
cv2.setMouseCallback('image',draw_circle)


while(1):
    #show the image so people can paint on it
    cv2.imshow('image',img2)
    #now replace the painted image on the original image
    img[int(h/2):h,0:w]=img2
    #save it to local file system for future use if any
    cv2.imwrite('road_marked.jpg',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()