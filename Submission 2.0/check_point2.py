import cv2
import math

img=cv2.imread('00130.jpeg')
y, x,_ = img.shape


print('length:',x)
print('width:',y)
diagnol_length = math.sqrt(x*x + y*y)


print('diagnol length',diagnol_length)
print('assuming angle of view:',120)


angle_per_pixel_wrt_diagnol=120/float(diagnol_length)
angle_per_pixel_wrt_width=120/float(y)

print('angle per pixel_wrt_diagnol:',angle_per_pixel_wrt_diagnol)
print('angle per pixel_wrt_width:',angle_per_pixel_wrt_width)


center_pixel_x,center_pixel_y=x/2,y/2

cv2.circle(img,(center_pixel_x,center_pixel_y),3,(0,244,33),2)
cv2.circle(img,(614,443),3,(0,244,33),2)


x_distance=abs(math.pow((center_pixel_x-614),2))
y_distance=abs(math.pow((center_pixel_y-443),2))


distance_between_center_and_center_roi=math.sqrt((x_distance+y_distance))
cv2.line(img,(614,443),(center_pixel_x,center_pixel_y),(255,0,0),4,2)
print(distance_between_center_and_center_roi)
print("approximate angle of image between camera and sign wrt diagnol:",(distance_between_center_and_center_roi*angle_per_pixel_wrt_diagnol))
print("approximate angle of image between camera and sign wrt width:",(distance_between_center_and_center_roi*angle_per_pixel_wrt_width))

cv2.imshow('point',img)
cv2.waitKey(0)

