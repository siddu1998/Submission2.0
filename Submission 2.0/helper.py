import cv2


def mouse_callback_get_cordinates(event,x,y,flags,frame):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(frame,(x,y),5,(255,0,0),-1)
        return {'x':x,'y':y}
