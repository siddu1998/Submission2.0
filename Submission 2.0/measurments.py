import cv2
import numpy as np



print("Welcome to Application 2.0")
print("press the number coresponding to perfrom the action")
print("1 : To get x,y cordinates")
print("2 : The area of selected region")
print("3 : The height and length of a region")

print("Choose")
option=input()
option=int(option)


kernel = np.ones((3, 3), np.uint8)



font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 1





def morphology(black_white, kernel):
    closing = cv2.morphologyEx(black_white, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    return opening


def _rgb_threshold(rgb, rgb_t=180):
    low_rgb = np.array([rgb_t, rgb_t, rgb_t])
    high_rgb = np.array([255, 255, 255])
    black_white = cv2.inRange(rgb, low_rgb, high_rgb)
    return black_white


def _drgb_threshold(img, drgb_t=30):
    blank_drgb = np.zeros(img.shape, np.uint8)
    b = np.array(img[:, :, 0], np.int)
    g = np.array(img[:, :, 1], np.int)
    r = np.array(img[:, :, 2], np.int)
    blank_drgb[:, :, 0] = np.absolute(np.subtract(b, r))
    blank_drgb[:, :, 1] = np.absolute(np.subtract(g, b))
    blank_drgb[:, :, 2] = np.absolute(np.subtract(r, g))
    lower = np.array([0, 0, 0])
    higher = np.array([drgb_t, drgb_t, drgb_t])
    mask = cv2.inRange(blank_drgb, lower, higher)
    return mask



def mouse_callback_get_cordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        data="x:{},y:{}".format(x,y)
        clone=img.copy()
        cv2.putText(clone,data,(10,500), font, 2,(0,0,0),2,cv2.LINE_AA)
        show("cloned",clone)
        print("x:{},y:{}".format(x,y))




refPt=[]
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt,cropping
    clone=img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping=True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        cropping=False
        
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", img)
    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        
        thresh_rgb=_rgb_threshold(roi, 180)
        thresh_rgb = morphology(thresh_rgb, kernel)

        thresh_Drgb = _drgb_threshold(roi)
        thresh_Drgb = morphology(thresh_Drgb, kernel)

        thresh = cv2.bitwise_and(thresh_rgb, thresh_Drgb)
        cnt_img,contours,hierarchy = cv2.findContours(thresh, 1, 2)

        if cnt_img is not None:
            cv2.imshow("CNT",cnt_img)
            cv2.imwrite("cnt.jpeg",cnt_img)
        else:
            print("No contour found sorry :-(")
        if len(contours)>0:
            cnt = contours[0]
            area = cv2.contourArea(cnt)
    print("area in pixels:",area)
    print("actual area of image based on image callibration (area * scale):",area)



            


    return 0 




img = cv2.resize(cv2.imread('00018.jpeg'),(1000,1000))


cv2.namedWindow('image')

if option==1:
     cv2.setMouseCallback('image',mouse_callback_get_cordinates)
     


elif option==2:
    cv2.setMouseCallback("image", click_and_crop)
    

else:
    print("more yet to come")
 



while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
