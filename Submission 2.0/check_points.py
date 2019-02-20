import cv2
import math

img=cv2.imread('00130.jpeg')
y, x,_ = img.shape


print('length:',x)
print('width:',y)
diagnol_length = math.sqrt(x*x + y*y)


print('diagnol length',diagnol_length)
print('assuming angle of view:',45)


angle_per_pixel=1

print('angle per pixel:',120/800)

center_pixel_x,center_pixel_y=x/2,y/2

cv2.circle(img,(center_pixel_x,center_pixel_y),3,(0,244,33),2)
cv2.circle(img,(614,443),3,(0,244,33),2)


x_distance=abs(math.pow(center_pixel_x,2)-math.pow(614,2))
y_distance=abs(math.pow(center_pixel_y,2)-math.pow(443,2))


distance_between_center_and_center_roi=math.sqrt(math.pow(x_distance,2)+math.pow(y_distance,2))
cv2.line(img,(614,443),(center_pixel_x,center_pixel_y),(255,0,0),4,2)
print(distance_between_center_and_center_roi)
print("approximate angle of image between camera and sign:",(distance_between_center_and_center_roi*angle_per_pixel))
print('press 0 once you note the angle')
cv2.imshow('point',img)
cv2.waitKey(0)

