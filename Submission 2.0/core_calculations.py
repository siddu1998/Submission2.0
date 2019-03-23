import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import distance

def get_distance_between_two_consecutive_images(cordinate_1,cordinate_2):
    return distance.euclidean(cordinate_1,cordinate_2)

def draw_boxes_and_points(image,sign_cordinates):
    #tl
    cv2.circle(image,(sign_cordinates[0],sign_cordinates[1]),3,(255,255,255),-1)
    #tr
    cv2.circle(image,(sign_cordinates[0]+sign_cordinates[2],sign_cordinates[1]),3,(0,0,0),-1)
    #br
    cv2.circle(image,(sign_cordinates[0]+sign_cordinates[2],sign_cordinates[1]+sign_cordinates[3]),3,(0,0,255),-1)
    #bl
    cv2.circle(image,(sign_cordinates[0],sign_cordinates[1]+sign_cordinates[3]),3,(255,0,0),-1)
    cv2.imshow("framee",image)
    points=[(sign_cordinates[0],sign_cordinates[1]),
            (sign_cordinates[0]+sign_cordinates[2],sign_cordinates[1]),
            (sign_cordinates[0]+sign_cordinates[2],sign_cordinates[1]+sign_cordinates[3]),
            (sign_cordinates[0],sign_cordinates[1]+sign_cordinates[3])]
    return image,points

def clear_distortions(img_before_distance):
    #distortion matrics
    mtx=[[1203.032354,0,720.0],[0,1284.609285,540.0],[0,0,1]]
    #mtx=[[2468.6668434782608,0,1228.876620888020],[0,2468.6668434782608,1012.976060035710],[0,0,1]] 
    #dist=[ 0.00125859 , 0 ,  -0.00010658,0 ]
    dist=[ 0,0,0,0 ]
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
            class_of_sign=['class']

    return [sign_top_left_x,sign_top_left_y,sign_width,sign_height,class_of_sign]


def find_center_of_sign(sign_details_list):
    sign_top_left_x=sign_details_list[0]
    sign_top_left_y=sign_details_list[1]
    sign_width=sign_details_list[2]
    sign_height=sign_details_list[3]
    location_sign=(int((sign_top_left_x+sign_top_left_x+sign_width)/2),int((sign_top_left_y+sign_top_left_y+sign_height)/2))
    return location_sign


def finding_relative_location_of_image(center_sign,image_width):
    if center_sign[0]<image_width/2:
        #print("sign is to the left of the vehicle")
        return -1
    elif center_sign[0]>image_width/2:
        #print("sign is to the right of the vehicle")
        return 1
    else:
        #print("sign is alligned with the optical axis")
        return 0

def distance_two_points_along_x(A,B):
    return A[0]-B[0]
def distance_two_points_along_y(A,B):
    return A[1]-B[1]


def trignometric_calculations(x1,x2,f,camera_cordinates_1,camera_cordinates_2):
    dst= get_distance_between_two_consecutive_images(camera_cordinates_1,camera_cordinates_2)   
    #print('The images are taken at a distance of {} m '.format(dst)) 
    l =  dst * x1/(x2-x1) 
    w = l * (x2)/f 
    #w--> how right or how left the sign is (x-axis)
    #l--> how ahead the sign is (y-axis)
    #print('how inclined:', w) #add to the x-cordinate
    #print('how ahead:', l) #add to the y-cordinate
    

    return (w,l)


def parsing_camrea_annotations(image,camera_annotations):
    camera_annotations=pd.read_csv(camera_annotations)
    #print(image)
    for index,row in camera_annotations.iterrows():
        if row["image_name"]==image:
            camera_cordinates_x=row['x']
            camera_cordinates_y=row['y']
    return (camera_cordinates_x,camera_cordinates_y)
            
def camera_to_sign(camera_cordinates,distancs_tuple,right_or_left):
    #if sign is to the right
    if right_or_left==1:
        return (camera_cordinates[0]-distancs_tuple[0],camera_cordinates[1]+distancs_tuple[1])
    #id sign is to the left
    elif right_or_left==-1:
        return (camera_cordinates[0]+distancs_tuple[0],camera_cordinates[1]+distancs_tuple[1])

    
#def error_analysis(predicted_cordinates):
    #print("---------------------------------------------------------")
    #print("Error analysis")
    #print("---------------------------------------------------------")
    #print("The predicted outcome after calculation is as follow {} {}".format(predicted_cordinates[0],predicted_cordinates[1]))
    

def calculation_of_distances(image_file_name_before_distance,image_file_name_after_distance,sign_annotations,camera_annotations,f=1203.032354):
    #load image     
    #print(image_file_name_before_distance,image_file_name_after_distance)
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
    #if we are dealing with the same image proceed as else inform and kill 
    if sign_after_distance[4]==sign_before_distance[4]:
        #Find center of sign
        center_before_distance = find_center_of_sign(sign_before_distance)
        center_after_distance  = find_center_of_sign(sign_after_distance)
        #distance between center and sign
        x1=distance_two_points_along_x(center_before_distance,image_center)
        x2=distance_two_points_along_x(center_after_distance,image_center)
        #getting camera_cordinates_to_calculate distance between images
        camera_cordinates=parsing_camrea_annotations(image_file_name_after_distance,camera_annotations)
        camera_cordinates_image_1=parsing_camrea_annotations(image_file_name_before_distance,camera_annotations)
        #getting distances from camera
        distance_tuple=trignometric_calculations(x1,x2,f,camera_cordinates_image_1,camera_cordinates)
        #understanding spatial location
        right_or_left = finding_relative_location_of_image(center_after_distance,image_width)
        #adding and subtracting images 
        final_positions = camera_to_sign(camera_cordinates,distance_tuple,right_or_left)
        #error_analysis(final_positions)
        return final_positions
    else:
        #print('Sorry, We could not find the same sign on both the images')
        return (0,0)

def calculation_of_distances_from_user_points(image_file_name_1,image_file_name_2,points_1,points_2,camera_annotations,f=2468.6668434782608):
    #load image     
    img_before_distance = cv2.imread(image_file_name_1)
    img_after_distance  = cv2.imread(image_file_name_2)
    #clear distortions
    img_before_distance = clear_distortions(img_before_distance)
    img_after_distance  = clear_distortions(img_after_distance)
    #calculate image center and dimensions
    image_height,image_width,_=img_before_distance.shape
    image_center = (int(image_width/2),int(image_height/2))
    #distance between image center and user cordinates
    x1=distance_two_points_along_x(points_1,image_center)
    x2=distance_two_points_along_x(points_2,image_center)
    #getting cameras cordinates
    camera_cordinates=parsing_camrea_annotations(image_file_name_1,camera_annotations)
    camera_cordinates_image_1=parsing_camrea_annotations(image_file_name_2,camera_annotations)
    #how far and how wide
    distance_tuple=trignometric_calculations(x1,x2,f,camera_cordinates_image_1,camera_cordinates)
    #understanding spatial location
    right_or_left = finding_relative_location_of_image(points_2,image_width)
    #adding and subtracting images 
    final_positions = camera_to_sign(camera_cordinates,distance_tuple,right_or_left)
    error_analysis(final_positions)
    return final_positions
