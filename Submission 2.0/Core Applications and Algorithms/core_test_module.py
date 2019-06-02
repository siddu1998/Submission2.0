import cv2
from core_calculations import *
import utm




img_before_file_name='0018767.jpg'
img_after_file_name='0018768.jpg'

sign_cordinates=parsing_annotations('1_sign_annotations.csv',img_before_file_name)
sign_cordinates_after=parsing_annotations('1_sign_annotations.csv',img_after_file_name)

# print(sign_cordinates)
center_cordinates_before=find_center_of_sign(sign_cordinates)
center_cordinates_after=find_center_of_sign(sign_cordinates_after)
# print(center_cordinates)
img=cv2.imread(img_before_file_name)
h,w,_=img.shape
# cv2.circle(img,center_cordinates,3,(0,0,233),2,-1)
# cv2.line(img,(int(w/2),0),(int(w/2),h),(0,233,233),4)
# cv2.imwrite('test_core.jpg',img)


#where is the sign located, right or left?
right_of_left=finding_relative_location_of_image(center_cordinates_before,w)
if(right_of_left==1):
    print('right')
elif(right_of_left==-1):
    print('left')
else:
    print('alligned with optical axis')



utm_=calculation_of_distances(img_before_file_name,img_after_file_name,'1_sign_annotations.csv','1_camera_cordinates.csv')
print(utm_)
gps=utm.to_latlon(utm_[0], utm_[1],16, 'N')
print(gps)