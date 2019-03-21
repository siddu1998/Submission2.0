import cv2
from core_calculations import *
from math import cos

image_file_name='0002879.jpg'
image = cv2.imread(image_file_name)
image_height,image_width,_=image.shape
vanishing_point = (int(image_width/2), int(image_height/2))

cv2.circle(image,vanishing_point,4,(0,0,0))
cv2.circle(image,(318,138),4,(0,0,0))

Y = abs(138-vanishing_point[1]) #pixels

H=2 #meters
f = 2468.6668434782608 #pixels
Z = (H*f)/Y #m *pixel/pixel == meters
X = abs(318-vanishing_point[0])

angle_beta = X/Z
print("inpath_distance:",Z)
print("cosine distance:", Z/cos(angle_beta))
camera_location=parsing_camrea_annotations(image_file_name,'i75_camera_cordinates.csv')
print(camera_location[1])
print(camera_location[1]+Z)

