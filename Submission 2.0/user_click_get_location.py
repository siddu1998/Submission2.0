import cv2
import numpy as np
import sys
import utm
from core_calculations import *
import gmplot
import argparse 
ap = argparse.ArgumentParser()
ap.add_argument("-im1", "--image_1", help = "Enter Image before distance")
ap.add_argument("-im2", "--image_2", help = "Enter Image after distance")
ap.add_argument("-r","--road",help="Enter expressway name")
args = vars(ap.parse_args())





ix_x,ix_y=-1,-1
iy_y,iy_y=-1,-1
image_1_points=0
image_2_points=0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix_x,ix_y,iy_x,iy_y,image_1_points,image_2_points
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(param,(x,y),15,(255,255,0),-1)
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
image_file_1=args['image_1']
x = cv2.imread(image_file_1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,x)

image_file_2=args['image_2']
y = cv2.imread(image_file_2)
cv2.namedWindow('imagey')
cv2.setMouseCallback('imagey',draw_circle,y)



while(1):
    cv2.imshow('image',x)
    cv2.imshow('imagey',y)
    cv2.imwrite('image_1.jpg',x)
    cv2.imwrite('image_2.jpg',y)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

print('{}_camera_cordinates.csv'.format(args['road']))
get_shit=calculation_of_distances_from_user_points(image_file_1,image_file_2,(ix_x,ix_y),(iy_x,iy_y),'{}_camera_cordinates.csv'.format(args['road']))

predicted_gps=utm.to_latlon(int(get_shit[0]),int(get_shit[1]), 16, 'N')
predicted_lat=predicted_gps[0]
predicted_long=predicted_gps[1]
print(predicted_gps)
gmap1 = gmplot.GoogleMapPlotter(predicted_lat, 
                                predicted_long, 13 ) 
  
# Pass the absolute path
#uncomment line number 77 to store map
#gmap1.draw( "C:\\Users\\msais\\Desktop\\map.html" )