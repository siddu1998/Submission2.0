import cv2
import math



fx =  2468.6668434782608

img=cv2.imread('0002875.jpg')
Y,X,_=img.shape

focal_length_in_mm = (fx*15)/X
print("{}mm".format(focal_length_in_mm))