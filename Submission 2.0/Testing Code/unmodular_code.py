
#reading focal lenghths of the image in pixels and mm
f=2468.6668434782608 

# before_image_str=str(input("Enter Image name before covering distance"))
# after_image_str=str(input("Enter Image name after covering a distance of 5m"))


image_file_name_before_distance = str(input("Please enter the file name of image before distance "))
image_file_name_after_distance  = str(input("Please enter the file name of image after distance "))

import cv2
import math
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 


#reading image
img_before_distance = cv2.imread(image_file_name_before_distance)
img_after_distance  = cv2.imread(image_file_name_after_distance)


        
#distortion matrics
mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]]
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

#converting into numpy
mtx = np.array(mtx)
dist=np.array(dist)

#image dimenstions
image_height,image_width,_=img_before_distance.shape

#pumping distortion matrix
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(image_width,image_height),1,(image_width,image_height))

#undistort image_before_distance
img_before_distance = cv2.undistort(img_before_distance, mtx, dist, None, newcameramtx)
x,y,w,h = roi
img_before_distance = img_before_distance[y:y+h, x:x+w]

#undistort image_after_distance
img_after_distance = cv2.undistort(img_after_distance, mtx, dist, None, newcameramtx)
x,y,w,h = roi
img_after_distance = img_after_distance[y:y+h, x:x+w]



#image center
image_center = (int(image_width/2),int(image_height/2))


#reading annotations file and finding location of sign in images
highway_sign_annotations = pd.read_csv('i75_sign_annotations.csv')

for index,row in highway_sign_annotations.iterrows():
    if row['frame_name']== image_file_name_before_distance:
        sign_1_top_left_x=row['top_x']
        sign_1_top_left_y=row['top_y']
        sign_1_width=row['width']
        sign_1_height=row['height']

    if row['frame_name']==image_file_name_after_distance:
        sign_2_top_left_x=row['top_x']
        sign_2_top_left_y=row['top_y']
        sign_2_width=row['width']
        sign_2_height=row['height']
        class_name_image_2=row['class']


location_sign_before_distance=(int((sign_1_top_left_x+sign_1_top_left_x+sign_1_width)/2),int((sign_1_top_left_y+sign_1_top_left_y+sign_1_height)/2))
location_sign_after_distance=(int((sign_2_top_left_x+sign_2_top_left_x+sign_2_width)/2),int((sign_2_top_left_y+sign_2_top_left_y+sign_2_height)/2))

#display images
cv2.rectangle(img_before_distance,(sign_1_top_left_x,sign_1_top_left_y),(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_2_height),(0,0,0),1)
cv2.rectangle(img_after_distance,(sign_2_top_left_x,sign_2_top_left_y),(sign_2_top_left_x+sign_2_width,sign_2_top_left_y+sign_2_height),(0,0,0),1)

#mark centers of signs
cv2.circle(img_before_distance,location_sign_before_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,location_sign_after_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,image_center,3,(255,0,0),4,-1)

#image center to sign center
cv2.line(img_before_distance,image_center,location_sign_before_distance,(0,0,0),5,-1)
cv2.line(img_after_distance,image_center,location_sign_after_distance,(0,0,0),5,-1)


#display images resize
img_before_distance=cv2.resize(img_before_distance,(500,500))
img_after_distance=cv2.resize(img_after_distance,(500,500))

cv2.imshow('image_before_distance', img_before_distance)
cv2.imshow('image_after_distance', img_after_distance)

cv2.waitKey(0)

#destroy all windoes
cv2.destroyAllWindows()


#Calculations

#distance_between_center_and_sign_along_x_before
x1=image_center[0]-location_sign_before_distance[0] #in pixels
#distance_between_center_and_sign_along_x_after
x2=image_center[0]-location_sign_after_distance[0] #in pixels


#calculate how far and how wide
l = 5 * x1/(x2-x1) # 5 in meters x1pixels/x2-x1pixels --> answer in meters
w = l * (x2)/f     # l in meters x2pixels/fpixels --->answer in meters  


print("l in m",l)
print("w in m",w)


#comparision

g_truth=(736465.7375,3750769.212)
camera=(736497.1112,3750738.772)

pred_1=(camera[0]+w,camera[1]+l)

#compare results
print("actual:",g_truth)
print("pred1:",pred_1)
print("x cordinate missing mark by: ",g_truth[0]-pred_1[0])
print("y_cordinate missing mark by:", g_truth[1]-pred_1[1])







