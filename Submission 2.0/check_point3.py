import cv2
import math
import numpy as np 
import matplotlib.pyplot as plt



#reading focal lenghths of the image in pixels and mm
f=2468.6668434782608 

#reading image
img_before_distance = cv2.imread('0002891.jpg')
img_after_distance = cv2.imread('0002892.jpg')


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
image_center = (image_width/2,image_height/2)

#location of signs in image,

sign_1_top_left_x=1707
sign_1_top_left_y=105
sign_1_width=69
sign_1_height=75

sign_2_top_left_x=1740
sign_2_top_left_y=111
sign_2_width=69
sign_2_height=78

location_sign_before_distance=((sign_1_top_left_x+sign_1_top_left_x+sign_1_width)/2,(sign_1_top_left_y+sign_1_top_left_y+sign_1_height)/2)
location_sign_after_distance=((sign_2_top_left_x+sign_2_top_left_x+sign_2_width)/2,(sign_2_top_left_y+sign_2_top_left_y+sign_2_height)/2)

#display images
cv2.rectangle(img_before_distance,(1707,105),(1707+69,105+75),(0,0,0),1)
cv2.rectangle(img_after_distance,(1740,111),(1740+69,111+78),(0,0,0),1)

#mark centers of signs
cv2.circle(img_before_distance,location_sign_before_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,location_sign_after_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,image_center,3,(255,0,0),4,-1)

# #image center to sign center
cv2.line(img_before_distance,image_center,location_sign_before_distance,(0,0,0),5,-1)
cv2.line(img_after_distance,image_center,location_sign_after_distance,(0,0,0),5,-1)


#dividing into quardrants

#horizontal
cv2.line(img_before_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4,-1)
cv2.line(img_after_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4)
#vertical
cv2.line(img_before_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)
cv2.line(img_after_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)

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
l = 5 * x1/(x2-x1) 
w = l * (x2)/f       


print("l in mm",l)
print("w in mm",w)


#comparision

g_truth=(732063.6161539537,3738027.0026369933)
camera=(732095.4582989508,3738103.923706733)

pred_1=(camera[0]+w,camera[1]+l)

#compare results
print("actual:",g_truth)
print("pred1:",pred_1)
print("x cordinate missing mark by: ",g_truth[0]-pred_1[0])
print("y_cordinate missing mark by:", g_truth[1]-pred_1[1])