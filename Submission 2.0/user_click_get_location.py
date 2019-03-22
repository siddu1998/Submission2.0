import cv2
import numpy as np
import sys


from core_calculations import *


ix_x,ix_y=-1,-1
iy_y,iy_y=-1,-1
image_1_points=0
image_2_points=0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix_x,ix_y,iy_x,iy_y,image_1_points,image_2_points
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(param,(x,y),4,(255,0,0),-1)
        if image_1_points==0:
            ix_x=x
            iy_y=y
            print('{},{} x and y from'.format(x,y))
            image_1_points=image_1_points+1
        elif image_2_points==0 and image_1_points==1:
            iy_x=x
            iy_y=y
            print('{},{} x and y from'.format(x,y))
            image_2_points=image_2_points+1
        else:
            print('Hmmm...are you sure you have choosen only one point from each image')
            sys.exit()


# Create a black image, a window and bind the function to window
image_file_1='0000750.jpg'
x = cv2.imread(image_file_1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,x)

image_file_2='0000751.jpg'
y = cv2.imread(image_file_2)
cv2.namedWindow('imagey')
cv2.setMouseCallback('imagey',draw_circle,y)



while(1):
    cv2.imshow('image',x)
    cv2.imshow('imagey',y)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


get_shit=calculation_of_distances_from_user_points(image_file_1,image_file_2,(ix_x,ix_y),(iy_x,iy_y),'i285_camera_cordinates.csv')
print(get_shit)