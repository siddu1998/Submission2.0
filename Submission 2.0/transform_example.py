from length_pavement import four_point_transform
import numpy as np
import argparse
import cv2
from core_calculations import *

# construct the argument parse and parse the arguments

 
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them

image_file_name="0002878.jpg"

sign_locations = parsing_annotations("i75_sign_annotations.csv",image_file_name)
image = cv2.imread(image_file_name)
_,pts = points=draw_boxes_and_points(image,sign_locations)
pts=np.array([(1214,255),(1255,255),(1255,0),(1214,0)], dtype = "float32")

# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
 
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)