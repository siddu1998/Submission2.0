import argparse
import cv2
 
refPt = []
cropping = False
i=0
distance = int(input("Please enter the distance between two consecutive images"))


def click_and_crop(event, x, y, flags, param):
        global refPt, cropping,i
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
                        i=i+1
                else:
                        cv2.imwrite('after_distance.jpeg',roi)

                

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True, help="Path to the image")
ap.add_argument("-i2", "--image2",required=True,help="Path to the second image")

args = vars(ap.parse_args())
 
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

x1, y1,_ = image_before_travelling_distance.shape
x2, y2,_ = image_after_travelling_distance.shape


print("Thanks for cropping: Your object size (in pixels) w.r.t to the image sensor is as follows")

print('Before moving a distance of d Image width of sign in approx x1:{} pixels:'.format(X1))
print('Before moving a distance of d Image height of sign in approx y1:{} pixels:'.format(Y1))

print('After moving a distance of d Image width of sign in approx x2:{} pixels:'.format(X2))
print('After moving a distance of d Image height of sign in approx y2:{} pixels:'.format(Y2))


