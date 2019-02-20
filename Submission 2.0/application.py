#Sai Siddartha Maram (Incoming Intern GTech)
"""
inputs :
        image1
        image2
        distance
output:
        approximate distance between image 
        sensor and tapped sign board
"""

"""
imports :
        argparse: to take in input images path and distance
        cv2     : computer vision 
        get_angle: from utility_functions for getting angle between pixel and sensor

"""
import argparse
import cv2
from utility_functions import (get_angle,get_distance_between_cordinates)


"""
taking input arguments --image1 --image2 --distance on terminal
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True, help="Path to the image")
ap.add_argument("-i2", "--image2",required=True,help="Path to the second image")
ap.add_argument("-i2", "--distance",required=True,help="distance between two consecutive images")

args = vars(ap.parse_args())



"""
global variables:
        refPt --> to get cropped region cordinates
        cropping --> flag to check status
        i       --> flag to check currently crooped imgae
        coi_1/2_x/y --> center of sign board pixels w.r.t image

"""
refPt = []
cropping = False
i=0

#center pixels of roi
coi_1_x=0
coi_1_y=0
coi_2_x=0
coi_2_y=0


"""
click_and_crop: 
        @param: mouse_event, mouse cordinates, param(here image)
        @role : Takes in image mouse cordinates of roi and crops in out
        @returns: saves roi in pwd
"""


def click_and_crop(event, x, y, flags, param):
        global refPt, cropping,i,coi_1_x,coi_1_y,coi_2_x,coi_2_y
        if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True
        
        elif event == cv2.EVENT_LBUTTONUP:
                refPt.append((x, y))
                cropping = False  
                cv2.rectangle(param, refPt[0], refPt[1], (0, 255, 0), 2)

                cv2.imshow("{}".format(param), param)

                roi = param[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                if i==0:
                        cv2.imwrite('before_distance.jpeg',roi)
                        
                        coi_1_x=(refPt[0][0]+refPt[1][0])/2
                        coi_1_y=(refPt[0][1]+refPt[1][1])/2
                        i=i+1
                else:
                        cv2.imwrite('after_distance.jpeg',roi)
                        coi_2_x=(refPt[0][0]+refPt[1][0])/2
                        coi_2_y=(refPt[0][1]+refPt[1][1])/2

                

 
print("User ROI selector, Please press 'O' once you are done!")
image1 = cv2.imread(args["image1"])
cv2.namedWindow("image1")
cv2.imshow("image1",image1)
cv2.setMouseCallback("image1", click_and_crop,image1)

image2 = cv2.imread(args["image2"])
cv2.namedWindow("image2")
cv2.imshow("image2",image2)
cv2.setMouseCallback("image2", click_and_crop,image2)


cv2.waitKey(0)
cv2.destroyAllWindows()


image_before_travelling_distance=cv2.imread('before_distance.jpeg')
image_after_travelling_distance=cv2.imread('after_distance.jpeg')

y1, x1,_ = image_before_travelling_distance.shape
y2, x2,_ = image_after_travelling_distance.shape


print("Thanks for cropping: Your object size (in pixels) w.r.t to the image sensor is as follows")

print('Before moving a distance of d Image width of sign in approx x1:{} pixels:'.format(x1))
print('Before moving a distance of d Image height of sign in approx y1:{} pixels:'.format(y1))

print('After moving a distance of d Image width of sign in approx x2:{} pixels:'.format(x2))
print('After moving a distance of d Image height of sign in approx y2:{} pixels:'.format(y2))
print('coi_x_1 : {}, coi_y_1 : {}'.format(coi_1_x,coi_1_y))
print('coi_x_2 : {}, coi_y_2 : {}'.format(coi_2_x,coi_2_y))

theta_1=get_angle(image1,coi_1_x,coi_1_y)
theta_2=get_angle(image2,coi_2_x,coi_2_y)


print("Estimated angle of device of sign from device before distance d: ",theta_1)
print("Estimated angle of device of sign from device after distance d: ",theta_2)



approx_final_distance_between_camera_and_sign= args["distance"] * (x1/float(abs(x2-x1)))
print(approx_final_distance_between_camera_and_sign)
