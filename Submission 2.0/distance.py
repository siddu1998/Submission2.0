import math
import numpy
from scipy.spatial import distance
camera_x_cordinate=736516.45814926
camera_y_cordinate= 3750734.29288626

pred_sign_x_cordinate=camera_x_cordinate+50
pred_sign_y_cordinate=camera_y_cordinate+11.26
predited=(pred_sign_x_cordinate,pred_sign_y_cordinate)
actual=(736465.73748737,3750769.21175686)
        
dst = distance.euclidean(predited, actual)
print(dst)

print(pred_sign_x_cordinate)
print(pred_sign_y_cordinate)



#hello