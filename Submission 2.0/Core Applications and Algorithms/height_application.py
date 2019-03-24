import cv2
import numpy as np

ix,iy = -1,-1
ix_1,iy_1=-1,-1
i=0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,ix_1,iy_1,i
    if event == cv2.EVENT_LBUTTONDBLCLK and i==0:
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        ix,iy = x,y
        i=i+1
    elif event == cv2.EVENT_LBUTTONDBLCLK and i==1:
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        ix_1,iy_1 = x,y
        i=i+1
    elif i>1:
        print('you have choosen two points')
        return 

# Create a black image, a window and bind the function to window
img = cv2.imread('0002877.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(ix,iy)
cv2.destroyAllWindows()

print(iy)
print(iy_1)
print('{} pixels'.format(abs(iy-iy_1)))