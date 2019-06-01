import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread('0015561.jpg')

plt.figure()
plt.imshow(img)
plt.show()

cv2.circle(img,(292,994),15,(0,255,255),4)
cv2.circle(img,(564,763),15,(0,255,255),4)
cv2.circle(img,(804,763),15,(0,255,255),4)
cv2.circle(img,(1008,956),15,(0,255,255),4)

cv2.line(img,(292,994),(564,763),(0,0,0),3)
cv2.line(img,(292,994),(1008,956),(0,0,0),3)
cv2.line(img,(564,763),(804,763),(0,0,0),3)
cv2.line(img,(804,763),(1008,956),(0,0,0),3)

h,w,_=img.shape
cv2.imwrite('points.jpg',img)

source_points=np.float32([ [292,994],[564,763],[804,763],[1008,956]  ])
destination_points = np.float32([ [0,1700], [0, 0], [230, 0], [230, 1700] ])


image=cv2.imread('points.jpg')
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (300,1700))
plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie.jpg",result)

mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]

ppx=300/3.6
Lh = np.linalg.inv(np.matmul(matrix, mtx))
pix_per_meter_y = ppx * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
print(ppx, pix_per_meter_y)
length=1700/pix_per_meter_y
print(length)




cv2.waitKey(0)