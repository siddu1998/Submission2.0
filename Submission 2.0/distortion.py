import cv2
import numpy as np

img= cv2.imread('0002876.jpg')


mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]]
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

mtx = np.array(mtx)
dist=np.array(dist)

h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)