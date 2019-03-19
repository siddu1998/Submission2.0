import cv2

image=cv2.imread("0002878.jpg")

IMAGE_H,IMAGE_W,_=image.shape
print(IMAGE_H)
print(IMAGE_W)
ORIGINAL_SIZE = IMAGE_W, IMAGE_H
UNWARPED_SIZE = 500, 600