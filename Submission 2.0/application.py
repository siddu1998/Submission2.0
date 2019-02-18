"""
@Sai Siddartha Maram
"""



import cv2
import sys
import argparse


"""
Input for the application demands, two images taken at a variable distance 'd'
"""

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
	help="image 1 from GT sensing vehicle")

ap.add_argument("-i2",'--image2',required=True,
        help="image 2 from GT sensing vehicle")

ap.add_argument("-dst",'--distance',required=True,
        help="distance between two consecutive images")

args = vars(ap.parse_args())
 
""" 
variable chart:
dst : distance between two consecutive images 
"""

dst = int(input)