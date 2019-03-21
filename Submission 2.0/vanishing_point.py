import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from birdseye import BirdsEye

import numpy as np
import cv2
def region_of_interest(img, vertices):
    # Define a blank matrix that matches the image height/width.
    mask = np.zeros_like(img)
    # Retrieve the number of color channels of the image.
    channel_count = img.shape[2]
    # Create a match color with the same color channel counts.
    match_mask_color = (255,) * channel_count
      
    # Fill inside the polygon
    cv2.fillPoly(mask, vertices, match_mask_color)
    
    # Returning the image only where mask pixels match
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('0017781.jpg')
plt.figure()
plt.imshow(image)
plt.show()
height,width,_=image.shape
region_of_interest_vertices = [
    (0, height),
    (659,715),
    (753,709),
    (width, height),
]

cropped_image = region_of_interest(
    image,
    np.array([region_of_interest_vertices], np.int32),
)
# cv2.line(image,(0,height),(int(width/2),int(height/2)),(255,255,255),3)
# cv2.line(image,(width,height),(int(width/2),int(height/2)),(255,255,255),3)

gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

cannyed_image = cv2.Canny(gray_image,100,130)


plt.figure()
plt.subplot(2,2,1)
plt.imshow(cropped_image)

plt.subplot(2,2,2)
plt.imshow(image)

plt.subplot(2,2,3)
plt.imshow(gray_image)


plt.subplot(2,2,4)
plt.imshow(cannyed_image)
plt.show()
#bl,tl,tr,br
#source_points=np.float32([ [0, height],[659,715],[753,709],[width, height]  ])
source_points=np.float32([ [620, 780],[637,734],[789,728],[813, 766]  ])
destination_points = np.float32([ [0, 600], [0, 0], [600, 0], [600, 600] ])
#destination_points = np.float32([ [0, 2048], [0, 0], [2248, 0], [2248, 2048] ])
print(type(destination_points))

matrix = cv2.getPerspectiveTransform(source_points, destination_points)
result = cv2.warpPerspective(cropped_image, matrix, (600,600))


plt.figure()
plt.imshow(result)
plt.show()
cv2.imwrite("birdie.jpg",result)

