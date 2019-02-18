import argparse
import cv2
 
refPt = []
cropping = False
i=0
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