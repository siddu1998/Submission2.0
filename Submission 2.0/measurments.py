
"""
@Sai Siddartha Maram
--------------------
The following module achieve the below mentioned tasks


1) the length (depth) of a pavement marking, and guardrail distance, 
2) the height of a sign post and a light pole, 
3) an area, pothole area or patched area,
4) x, y coordinates of a point (by pointing to a location)

"""



import cv2
import numpy as np




""""
some global utility variables
"""
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 1


def mouse_callback_get_cordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        print("x:{},y:{}".format(x,y))




reference_points=[]
cropping=False


def click_and_crop




img = cv2.imread('00018.jpeg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_callback_get_cordinates)


while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
