import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = mpimg.imread('0017781.jpg')
plt.figure()
plt.imshow(image)
plt.show()

height,width,_=image.shape

source_points=np.float32([ [620, 780],[637,734],[789,728],[813, 766]  ])
destination_points = np.float32([ [0, 600], [0, 0], [600, 0], [600, 600] ])

#source_points=np.float32([ [0, height],[659,715],[753,709],[width, height]  ])
#destination_points = np.float32([ [0, 2048], [0, 0], [2248, 0], [2248, 2048] ])
print(type(destination_points))

matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(image, matrix, (600,600))


plt.figure()
plt.imshow(result)
plt.show()


