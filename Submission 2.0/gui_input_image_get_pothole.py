from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from tkinter import filedialog
import cv2
from PIL import Image
from PIL import ImageTk


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
                cv2.imshow("cropped", param)
                
                clone = param.copy()
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.imshow("ROI", roi)
                cv2.imwrite('marking.jpg',roi)
                cv2.waitKey(0)
    


def show_entry_fields():
    global panelA
    global path_a
    
    bl_x = e_bl_x.get()
    bl_y = e_bl_y.get()

    tl_x    = e_tl_x.get()
    tl_y    = e_tl_y.get()

    tr_x   = e_tr_x.get()
    tr_y   = e_tr_y.get()

    br_x= e_br_x.get()
    br_y= e_br_y.get() 

    bl_x=int(bl_x)
    bl_y=int(bl_y)
    tl_x=int(tl_x)
    tr_y=int(tr_y)
    br_x=int(br_x)
    br_y=int(br_y)
    

    source_points=np.float32([ [bl_x,bl_y],[tl_x,tl_y],[tr_x,tr_y],[br_x,br_y]  ])
    destination_points = np.float32([ [0, 600], [0, 0], [600, 0], [600, 600] ])

    image=cv2.imread(path_a)
    
    matrix = cv2.getPerspectiveTransform(source_points, destination_points)
    result = cv2.warpPerspective(image, matrix, (600,600))
    result_image_y,result_image_x,_=result.shape
    cv2.imwrite('birdie.jpg',result)
    result=Image.fromarray(result)
    result=result.resize((250, 250), Image.ANTIALIAS)
    result=ImageTk.PhotoImage(result)
    mtx=[[1203.032354,0,720.0],[0,1284.609285,540.0],[0,0,1]]
    dist=[ 0,0,0,0 ]
    Lh = np.linalg.inv(np.matmul(matrix, mtx))
    bird = cv2.imread('birdie.jpg')
    cv2.imshow("image", bird)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop,bird)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pothole=cv2.imread('marking.jpg')

    pothole_y_pixels,pothole_x_pixels,_=pothole.shape
    print(pothole_y_pixels,pothole_x_pixels)
    pix_per_meter_x = result_image_x/3.5
    pix_per_meter_y = pix_per_meter_x * np.linalg.norm(Lh[:,0]) / np.linalg.norm(Lh[:,1])
    print(pix_per_meter_x, pix_per_meter_y)

    print(pothole_y_pixels)
    print(pothole_x_pixels)
    print('height {}m'.format(pothole_y_pixels/pix_per_meter_y))
    print('length {}m'.format(pothole_x_pixels/171))



    if panelA is None:
            panelA=Label(image=result)
            panelA.image=result
            panelA.grid(row=12)


   
master = Tk()


#bl,tl,tr,br
Label(master, text="bottom left x").grid(row=0)
Label(master, text="bottom left y").grid(row=1)
Label(master, text="top left x").grid(row=2)
Label(master, text="top left y").grid(row=3)
Label(master, text="top right x").grid(row=4)
Label(master, text="top right y").grid(row=5)
Label(master, text="bottom right x").grid(row=6)
Label(master, text="bottom right y").grid(row=7)


#Bottom Left Entry
e_bl_x = Entry(master)
e_bl_y = Entry(master)
#Top left text entry
e_tl_x = Entry(master)
e_tl_y = Entry(master)
#Top righ text entry
e_tr_x = Entry(master)
e_tr_y = Entry(master)
#Bottom right text entry
e_br_x = Entry(master)
e_br_y = Entry(master)


#Bottom Left text location
e_bl_x.grid(row=0, column=1)
e_bl_y.grid(row=1, column=1)
#Top left
e_tl_x.grid(row=2, column=1)
e_tl_y.grid(row=3, column=1)
#Top Right
e_tr_x.grid(row=4, column=1)
e_tr_y.grid(row=5, column=1)
#Bottom Right
e_br_x.grid(row=6, column=1)
e_br_y.grid(row=7, column=1)

panelA=None

Button(master, text='Quit', command=master.quit).grid(row=8, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=8, column=1, sticky=W, pady=4)
path_a = filedialog.askopenfilename()
image = mpimg.imread(path_a)
plt.figure()
plt.imshow(image)
plt.show()




mainloop( )