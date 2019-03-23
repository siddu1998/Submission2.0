import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2
from tkinter import filedialog
from core_calculations import *



def select_image():
    global panelA,panelB
    path_a = filedialog.askopenfilename()
    path_b = filedialog.askopenfilename()
    print(path_a[-11:],path_b[-11:])
    if len(path_a)>0 and len(path_b)>0:
        image_before_distance=cv2.imread(path_a)
        image_after_distance=cv2.imread(path_b)
        image_before_distance=Image.fromarray(image_before_distance)
        image_after_distance=Image.fromarray(image_after_distance)
        
        image_before_distance=image_before_distance.resize((250, 250), Image.ANTIALIAS)
        image_after_distance=image_after_distance.resize((250,250),Image.ANTIALIAS)

        image_before_distance=ImageTk.PhotoImage(image_before_distance)
        image_after_distance=ImageTk.PhotoImage(image_after_distance)
        
        if panelA is None or panelB is None:
            result=(calculation_of_distances(path_a[-11:],path_b[-11:],"0_sign_annotations.csv","0_camera_cordinates.csv"))
            result_to_display_x =tk.Label(root,text="X predicted:{}".format(result[0]))
            result_to_display_x.pack(padx=5, pady=10, side='left') 
        


            result_to_display_y =tk.Label(root,text='Y Predicted:{}'.format(result[1]))
            result_to_display_y.pack(padx=5, pady=20, side='left') 

            panelA=tk.Label(image=image_before_distance)
            panelA.image=image_before_distance
            panelA.pack(side="left",pady=15)
            

            panelB=tk.Label(image=image_after_distance)
            panelB.image=image_after_distance
            panelB.pack(side="right",pady=15)

        
            
    else:
        result=(calculation_of_distances(path_a[-11:],path_b[-11:],"0_sign_annotations.csv","0_camera_cordinates.csv"))
        result_to_display_x =tk.Label(root,text="X predicted:{}".format(result[0]))
        result_to_display_x.pack(padx=5, pady=10, side='left') 


        result_to_display_y =tk.Label(root,text='Y predicted:{}'.format(result[1]))
        result_to_display_y.pack(padx=5, pady=20, side='left') 

        panelA.configure(image=image_before_distance)
        panelB.configure(image=image_after_distance)
        panelA.image=image_before_distance
        panelB.image=image_after_distance




root = tk.Tk()
panelA=None
panelB=None

btn_for_pothole=tk.Button(root,text="Pothole Area Calculation on Interstate",command=select_image)
btn_for_pothole.pack(side="bottom", fill="both", padx="10", pady="10")

image = tk.PhotoImage(file="logo.png")
label = tk.Label(image=image)
label.pack(side='bottom',fill='both',padx="10",pady="10")


# kick off the GUI
root.mainloop()