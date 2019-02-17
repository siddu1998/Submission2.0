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



font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 1


def mouse_callback_get_cordinates(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        print("x:{},y:{}".format(x,y))




refPt=[]
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt,cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        print("button pressed")
        print("appeding",x,y)
        refPt.append((x,y))
        cropping=True

    elif event == cv2.EVENT_LBUTTONUP:
        print("button released")
        print("appeding",x,y)
        refPt.append((x,y))
        cropping=False

        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", img)
        print("Storing image to find area")
    
        roi = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv2.imshow("ROI", roi)
        cv2.imwrite("area.jpg",roi)

        to_draw_contors=cv2.imread("area.jpg",0)
        ret,thresh = cv2.threshold(to_draw_contors,127,255,0)
        cnt_img,contours,hierarchy = cv2.findContours(thresh, 1, 2)
        cv2.imshow('contor',cnt_img)
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        print("area:",area)
        
    return 0 




img = cv2.imread('stop.jpg')
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
