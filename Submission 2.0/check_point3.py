import cv2
import math
import numpy as np 


#reading focal lenghths of the image
fx=2468.6668434782608

#reading image
img_before_distance = cv2.imread('0002875.jpg')
img_after_distance = cv2.imread('0002876.jpg')


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

#location of signs in image
location_sign_before_distance=((591+591+42)/2,(102+102+69)/2)
location_sign_after_distance=((531+531+51)/2,(108+108+69)/2)

#display images
cv2.rectangle(img_before_distance,(591,102),(591+42,102+69),(0,0,0),1)
cv2.rectangle(img_after_distance,(531,108),(531+51,108+69),(0,0,0),1)

#mark centers of signs
cv2.circle(img_before_distance,location_sign_before_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,location_sign_after_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,image_center,3,(255,0,0),4,-1)

#image center to sign center
cv2.line(img_before_distance,image_center,location_sign_before_distance,(0,0,0),5,-1)
cv2.line(img_after_distance,image_center,location_sign_after_distance,(0,0,0),5,-1)


#dividing into quardrants
cv2.line(img_before_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4,-1)
cv2.line(img_after_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4)
cv2.line(img_before_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)
cv2.line(img_after_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)

#display images
cv2.imshow('image_before_distance', img_before_distance)
cv2.imshow('image_after_distance', img_after_distance)


#destroy all windoes
cv2.destroyAllWindows()


#Calculations

#distance_between_center_and_sign_along_x_before
x1=image_center[0]-location_sign_before_distance[0]
#distance_between_center_and_sign_along_x_after
x2=image_center[0]-location_sign_after_distance[0]


#calculate how far and how wide
l = 5 * x1/(x2-x1)
w = l * x2/fx


print(l)
print(w)

#comparision
g_truth=(736465.73748737,3750769.21175686)
camera_x_cordinate=736516.45814926
camera_y_cordinate= 3750734.29288626
camera=(camera_x_cordinate,camera_y_cordinate)
pred_1=(camera[0]-w,camera[1]+l)


#compare results
print("actual:",g_truth)
print("pred1:",pred_1)

