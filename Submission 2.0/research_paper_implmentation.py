import cv2
from core_calculations import *
from math import cos

image_file_name='0002879.jpg'
image = cv2.imread(image_file_name)
image_height,image_width,_=image.shape
vanishing_point = (image_height/2, image_height/2)

Y = abs(332-vanishing_point[1]) #pixels
print(Y)
H=1.85 #meters
f = 2468.6668434782608
Z = (H*f)/Y
X = abs(339-vanishing_point[0])

angle_beta = X/Z
print("inpath_distance:",Z)
print("cosine distance:", Z/cos(angle_beta))





