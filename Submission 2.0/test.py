import cv2
import argparse
import numpy as np 



roi_1=[]

def click_and_crop(event,x,y,flags,param):
    global roi_1
    refPt=[]
    cropping=False
    if event==cv2.EVENT_LBUTTONDOWN:
        
        refPt.append((x, y))
        print(refPt)
        cropping=True
        
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        cropping=False
        print(refPt)
        roi_1=refPt
 
img=cv2.imread('00130.jpeg')
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
print(roi_1)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break