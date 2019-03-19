import math

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def clear_distortions(img_before_distance):
    #distortion matrics
    mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
    dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]
    #converting into numpy
    mtx = np.array(mtx)
    dist=np.array(dist)
    #image dimenstions
    image_height,image_width,_=img_before_distance.shape

    #pumping distortion matrix
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(image_width,image_height),1,(image_width,image_height))

    #undistort image_before_distance
    img_before_distance = cv2.undistort(img_before_distance, mtx, dist, None, newcameramtx)
    x,y,w,h = roi
    undistorted_image = img_before_distance[y:y+h, x:x+w]

    #undistort image_after_distance

    return undistorted_image

    

def parsing_annotations(highway_sign_annotations,image_file_name):
    highway_signs = pd.read_csv(highway_sign_annotations)
    for index,row in highway_signs.iterrows():
        if row['frame_name']== image_file_name:
            sign_top_left_x=row['top_x']
            sign_top_left_y=row['top_y']
            sign_width=row['width']
            sign_height=row['height']

    return [sign_top_left_x,sign_top_left_y,sign_width,sign_height]


def find_center_of_sign(sign_details_list):
    sign_top_left_x=sign_details_list[0]
    sign_top_left_y=sign_details_list[1]
    sign_width=sign_details_list[2]
    sign_height=sign_details_list[3]
    location_sign=(int((sign_top_left_x+sign_top_left_x+sign_width)/2),int((sign_top_left_y+sign_top_left_y+sign_height)/2))
    return location_sign


def finding_relative_location_of_image(center_sign):
    if center_sign[0]<1024:
        print("sign is to the left of the vehicle")
        return -1
    elif center_sign[0]>1024:
        print("sign is to the right of the vehicle")
        return 1
    else:
        print("sign is alligned with the optical axis")
        return 0

def distance_two_points_along_x(A,B):
    return A[0]-B[0]
def distance_two_points_along_y(A,B):
    return A[1]-B[1]


def trignometric_calculations(x1,x2,f):
    
    l = 5 * x1/(x2-x1) 
    w = l * (x2)/f 
    return (w,l)


def parsing_camrea_annotations(image,camera_annotations):
    camera_annotations=pd.read_csv(camera_annotations)
    print(image)
    for index,row in camera_annotations.iterrows():
        if row["image_name"]==image:
            camera_cordinates_x=row['x']
            camera_cordinates_y=row['y']
    return (camera_cordinates_x,camera_cordinates_y)
            
def camera_to_sign(camera_cordinates,distancs_tuple):
     return (camera_cordinates[0]+distancs_tuple[0],camera_cordinates[1]+distancs_tuple[1])


def error_analysis(predicted_cordinates):


    print("---------------------------------------------------------")
    print("Error analysis")
    print("---------------------------------------------------------")
    print("The predicted outcome after calculation is as follow {} {}".format(predicted_cordinates[0],predicted_cordinates[1]))
    

def calculation_of_distances(image_file_name_before_distance,image_file_name_after_distance,sign_annotations,camera_annotations,f=2468.6668434782608,d=5):
    #load image     
    img_before_distance = cv2.imread(image_file_name_before_distance)
    img_after_distance  = cv2.imread(image_file_name_after_distance)
    
    #clear distortions
    img_before_distance = clear_distortions(img_before_distance)
    img_after_distance  = clear_distortions(img_after_distance)
    
    #calculate image center and dimensions
    image_height,image_width,_=img_before_distance.shape
    image_center = (int(image_width/2),int(image_height/2))

    #parse annotations for details
    sign_before_distance = parsing_annotations(sign_annotations,image_file_name_before_distance)
    sign_after_distance  = parsing_annotations(sign_annotations,image_file_name_after_distance)
    #Find center of sign
    center_before_distance = find_center_of_sign(sign_before_distance)
    center_after_distance  = find_center_of_sign(sign_after_distance)
 

    #distance between center and sign
    x1=distance_two_points_along_x(center_before_distance,image_center)
    x2=distance_two_points_along_x(center_after_distance,image_center)
    distance_tuple=trignometric_calculations(x1,x2,f)
    
    
    camera_cordinates=parsing_camrea_annotations(image_file_name_after_distance,camera_annotations)
    final_positions = camera_to_sign(camera_cordinates,distance_tuple)

    error_analysis(final_positions)
    return final_positions


