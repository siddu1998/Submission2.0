from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
from tkinter import filedialog
from core_calculations import *

def select_image():
    global panelA,panelB,positions
    path_a = filedialog.askopenfilename()
    print(path_a[-11:])
    path_b = filedialog.askopenfilename()
    print(path_b[-11:])
    if len(path_a)>0 and len(path_b)>0:
        image_before_distance=cv2.imread(path_a)
        image_after_distance=cv2.imread(path_b)
        print(calculation_of_distances("0002878.jpg","0002879.jpg","i75_sign_annotations.csv","i75_camera_cordinates.csv"))
        image_before_distance=Image.fromarray(image_before_distance)
        image_after_distance=Image.fromarray(image_after_distance)
        
        image_before_distance=image_before_distance.resize((250, 250), Image.ANTIALIAS)
        image_after_distance=image_after_distance.resize((250,250),Image.ANTIALIAS)

        image_before_distance=ImageTk.PhotoImage(image_before_distance)
        image_after_distance=ImageTk.PhotoImage(image_after_distance)
        
        if panelA is None or panelB is None:
            panelA=Label(image=image_before_distance)
            panelA.image=image_before_distance
            panelA.pack(side="left",padx=10,pady=10)

            panelB=Label(image=image_after_distance)
            panelB.image=image_after_distance
            panelB.pack(side="right",padx=10,pady=10)
    else:
        panelA.configure(image=image_before_distance)
        panelB.configure(image=image_after_distance)
        panelA.image=image_before_distance
        panelB.image=image_after_distance


root= Tk()
panelA=None
panelB=None
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

# kick off the GUI
root.mainloop()