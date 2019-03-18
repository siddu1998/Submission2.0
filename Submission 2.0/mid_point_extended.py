import cv2
import pandas as pd


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (int(x), int(y))


ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        ix,iy = x,y
        
        
img=cv2.imread('0002878.jpg')
highway_sign_annotations = pd.read_csv('i75_sign_annotations.csv')
image_height,image_width,_=img.shape

for index,row in highway_sign_annotations.iterrows():
    if row['frame_name']=='0002878.jpg':
        sign_1_top_left_x=row['top_x']
        sign_1_top_left_y=row['top_y']
        sign_1_width=row['width']
        sign_1_height=row['height']
cv2.rectangle(img,(sign_1_top_left_x,sign_1_top_left_y),(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(0,0,0),4)
# cv2.line(img,(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(int(image_width/2),int(image_height/2)),(255,255,255))
# cv2.line(img,(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(image_width,sign_1_top_left_y+sign_1_height),(255,255,255))

cv2.namedWindow('image')
print("Point to the bottom of the sign using your mouse")
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        print(ix,iy)
        cv2.line(img,(ix,iy),(image_width,iy),(0,255,255),2)
        cv2.line(img,(int(image_width/2),0),(int(image_width/2),image_height),(0,0,0))        
        cv2.imwrite('road_marked.jpg',img)
        break
    elif k == ord('a'):
        print(ix,iy)
cv2.destroyAllWindows()

print("contact_point road and sign on the road x:",ix)
print("contact_point road and sign on the road y:",iy)


A=(ix,iy)
B=(image_width,iy)
C=(int(image_width/2),0)
D=(int(image_width/2),image_height)


find_distance_of_this_point=line_intersection((A, B), (C, D))
print("Point of curiousity",find_distance_of_this_point)
img=cv2.imread("road_marked.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)


