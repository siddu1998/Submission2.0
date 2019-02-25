import cv2
import math


fx =  2468.6668434782608

img=cv2.imread('0002875.jpg')
Y,X,_=img.shape

print('height of the image: Y',Y)
print('width of the image: X',X)

tan_theta_x_by_two = X/2 / fx

print(tan_theta_x_by_two)