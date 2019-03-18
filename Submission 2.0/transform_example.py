from transform import four_point_transform
import numpy as np 
import argparse 
import cv2
import pandas as pd


image=cv2.imread("0002878.jpg")






#reading annotations file and finding location of sign in images
highway_sign_annotations = pd.read_csv('i75_sign_annotations.csv')

for index,row in highway_sign_annotations.iterrows():
    if row['frame_name']=='0002878.jpg':
        sign_1_top_left_x=row['top_x']
        sign_1_top_left_y=row['top_y']
        sign_1_width=row['width']
        sign_1_height=row['height']


image_height,image_width,_=image.shape
pts = np.array(([(sign_1_top_left_x, sign_1_top_left_y), (sign_1_top_left_x+sign_1_width, sign_1_top_left_y), (sign_1_top_left_x+sign_1_width, sign_1_top_left_y-sign_1_height), (sign_1_top_left_x,sign_1_top_left_y-sign_1_height)]), dtype = "float32")
warped = four_point_transform(image, pts)
 
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)