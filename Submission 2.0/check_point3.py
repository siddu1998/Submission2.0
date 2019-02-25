import cv2



img_before_distance = cv2.imread('0002875.jpg')
img_after_distance = cv2.imread('0002876.jpg')

image_height,image_width,_=img_before_distance.shape


image_center = (image_width/2,image_height/2)


location_sign_before_distance=((591*2+42)/2,(102*2+69)/2)
location_sign_after_distance=((531*2+51)/2,(108*2+69)/2)


cv2.rectangle(img_before_distance,(591,102),(591+42,102+69),(0,0,0),1)
cv2.rectangle(img_after_distance,(531,108),(531+51,108+69),(0,0,0),1)

cv2.circle(img_before_distance,location_sign_before_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,location_sign_after_distance,3,(255,0,0),4)
cv2.circle(img_after_distance,image_center,3,(255,0,0),4,-1)

cv2.line(img_before_distance,image_center,location_sign_before_distance,(0,0,0),5,-1)
cv2.line(img_after_distance,image_center,location_sign_after_distance,(0,0,0),5,-1)

cv2.line(img_before_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4,-1)
cv2.line(img_after_distance,(image_width/2,0),(image_width/2,image_height),(0,0,0),4)

cv2.line(img_before_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)
cv2.line(img_after_distance,(0,image_height/2),(image_width,image_height/2),(0,0,0),4,-1)

img_before_distance=cv2.resize(img_before_distance,(1000,1000))
img_after_distance=cv2.resize(img_after_distance,(1000,1000))


cv2.imshow('image_before_distance', img_before_distance)
cv2.imshow('image_after_distance', img_after_distance)


print(image_center[0])
print("location of center of sign before:",location_sign_before_distance[0])
print("location of center of sign after:",location_sign_after_distance[0])

d_f_c_b_d = image_center[0]-location_sign_before_distance[0]
d_f_c_a_d = image_center[0]-location_sign_after_distance[0]

print("center-sign distance before in pixels:",d_f_c_b_d)
print("center-sign distance after in pixels:",d_f_c_a_d)



cv2.waitKey(0)
cv2.destroyAllWindows()