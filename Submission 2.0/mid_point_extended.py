import cv2
import pandas as pd


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
cv2.line(img,(int(image_width/2),0),(int(image_width/2),image_height),(0,0,0))
cv2.rectangle(img,(sign_1_top_left_x,sign_1_top_left_y),(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(0,0,0),4)
cv2.line(img,(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(int(image_width/2),int(image_height/2)),(255,255,255))
cv2.line(img,(sign_1_top_left_x+sign_1_width,sign_1_top_left_y+sign_1_height),(image_width,sign_1_top_left_y+sign_1_height),(255,255,255))

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    print("saving")
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        print(ix,iy)
        cv2.imwrite('road_marked.jpg',img)
        break
    elif k == ord('a'):
        print(ix,iy)
cv2.destroyAllWindows()

print("point on the road x:",ix)
print("point on the road y:",iy)