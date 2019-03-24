import cv2
import numpy as numpy



point1=(0,0)
point2=(0,0)



def mouse_callback_get_cordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(param,(x,y),5,(255,0,0),-1)
        print("x:{},y:{}".format(x,y))


