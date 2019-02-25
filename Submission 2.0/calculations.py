import cv2
import math



fx =  2468.6668434782608

img=cv2.imread('0002875.jpg')
Y,X,_=img.shape

print(fx)
print(X)
print('height of the image: Y',Y)
print('width of the image: X',X)

focal_length_in_mm = fx/X
print(focal_length_in_mm)