import cv2
from core_calculations import *
from math import cos

image_file_name='0003220.jpg'
image = cv2.imread(image_file_name)
image_height,image_width,_=image.shape
vanishing_point = (int(image_width/2), int(image_height/2))
sign_location=parsing_annotations('i_sign_annotations.csv',image_file_name)
sign_center=find_center_of_sign(sign_location)

cv2.circle(image,vanishing_point,7,(0,0,0),-1)
cv2.circle(image,sign_center,7,(0,0,0),-1)

Y = abs(sign_center[1]-vanishing_point[1]) #pixels

H=2 #meters
f = 2468.6668434782608 #pixels
Z = (H*f)/Y #m *pixel/pixel == meters
X = abs(sign_center[0]-vanishing_point[0])
image=cv2.resize(image,(1000,1000))
cv2.imshow('imag',image)
cv2.waitKey(0)
angle_beta = X/Z
print("inpath_distance:",Z)
print("cosine distance:", Z/cos(angle_beta))
camera_location=parsing_camrea_annotations(image_file_name,'i_camera_cordinates.csv')
print(camera_location[1])
print(camera_location[1]+Z)

