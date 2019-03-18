import cv2
import numpy as np
import matplotlib.pyplot as plt
#distortion matrics
mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]]
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

#converting into numpy
mtx = np.array(mtx)
dist=np.array(dist)
img1=cv2.imread('0002878.jpg')
img=cv2.imread('0002878.jpg')

#image dimenstions
image_height,image_width,_=img.shape

#pumping distortion matrix
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(image_width,image_height),1,(image_width,image_height))

#undistort image_before_distance
img = cv2.undistort(img, mtx, dist, None, newcameramtx)
x,y,w,h = roi
img = img[y:y+h, x:x+w]
cv2.imshow('image',img)

src = np.float32([[0, image_height], [image_width, image_height], [0, 0], [image_width, 0]])
dst = np.float32([[1214, 255], [1234, 255], [0, 0], [image_width, 0]])
img = img[0:(0+image_height), 0:image_width] # Apply np slicing for ROI crop
M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

warped_img = cv2.warpPerspective(img, M, (image_width, image_height)) # Image warping
plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB)) # Show results
plt.show()