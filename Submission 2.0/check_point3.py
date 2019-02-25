import cv2

img_before_distance = cv2.imread('0002875.jpg')
img_after_distance = cv2.imread('0002876.jpg')

cv2.rectangle(img_before_distance,(591,102),(591+42,102+69),(0,0,0),1)
cv2.rectangle(img_after_distance,(531,108),(531+51,108+69),(0,0,0),1)



cv2.imshow('image_before_distance',img_before_distance)
cv2.imshow('image_after_distance',img_after_distance)


cv2.waitKey(0)
cv2.destroyAllWindows()