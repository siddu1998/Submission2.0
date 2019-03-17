import pandas as pd

sign_annotations="i75_sign_annotations.csv"
annotation_data=pd.read_csv("i75_sign_annotations.csv")


for index, row in annotation_data.iterrows():
    if row['frame_name']=="0002891.jpg":
        top_x_before_distance=row['top_x']
        top_y_before_distance=row['top_y']
        width=row['width']
        height=row['height']
        class_name=row['class']

print(top_x_before_distance,top_y_before_distance,width,height,class_name)