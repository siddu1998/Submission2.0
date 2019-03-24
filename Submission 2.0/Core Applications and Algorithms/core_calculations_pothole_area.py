import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = mpimg.imread('0017781.jpg')
plt.figure()
plt.imshow(image)
plt.show()

height,width,_=image.shape

#source_points=np.float32([ [611, 780],[611,734],[789,728],[813, 766]  ])
source_points=np.float32([ [585, 792],[634,728],[772,713],[848,777]  ])
destination_points = np.float32([ [0, 600], [0, 0], [600, 0], [600, 600] ])

#source_points=np.float32([ [0, height],[659,715],[753,709],[width, height]  ])
#destination_points = np.float32([ [0, 2048], [0, 0], [2248, 0], [2248, 2048] ])
print(type(destination_points))

matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (600,600))


plt.figure()
plt.imshow(result)
plt.show()
# mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
# dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

mtx=[[1203.032354,0,720.0],[0,1284.609285,540.0],[0,0,1]]
dist=[ 0,0,0,0 ]

Lh = np.linalg.inv(np.matmul(matrix, mtx))
pix_per_meter_y = 171 * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(171, pix_per_meter_y)


