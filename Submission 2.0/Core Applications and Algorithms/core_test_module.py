import cv2
from core_calculations import *


img_file_name='0018705.jpg'
sign_cordinates=parsing_annotations('1_sign_annotations.csv',img_file_name)
print(sign_cordinates)
center_cordinates=find_center_of_sign(sign_cordinates)
print(center_cordinates)
img=cv2.imread(img_file_name)
h,w,_=img.shape
cv2.circle(img,center_cordinates,3,(0,0,233),2,-1)
cv2.line(img,(int(w/2),0),(int(w/2),h),(0,233,233),4)
cv2.imwrite('test_core.jpg',img)





#where is the sign located, right or left?

right_of_left=finding_relative_location_of_image(center_cordinates,w)
if(right_of_left==1):
    print('right')
elif(right_of_left==-1):
    print('left')
else:
    print('alligned with optical axis')