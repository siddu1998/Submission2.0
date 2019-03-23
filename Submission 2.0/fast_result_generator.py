import cv2
from core_calculations import *


a = '18625'
for i in range(0,143):
    zerios='00'
    image_1=zerios+str(a)+'.jpg'
    a=int(a)+1
    image_2 = zerios + str(a)+'.jpg'
    #print(image_1,image_2)
    print(calculation_of_distances(image_1,image_2,'1_sign_annotations.csv','1_camera_cordinates.csv'))
    
