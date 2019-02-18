import argparse
import cv2
 
refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
        global refPt, cropping
        if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True
        
        elif event == cv2.EVENT_LBUTTONUP:
                refPt.append((x, y))
                cropping = False  
                cv2.rectangle(param, refPt[0], refPt[1], (0, 255, 0), 2)
                cv2.imshow("image", param)
                
                clone = image.copy()
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.imshow("ROI", roi)
                cv2.waitKey(0)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop,image)
cv2.destroyAllWindows()