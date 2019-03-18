import cv2


string_1 = str(input("please enter the file name"))


img=cv2.imread(string_1)
cv2.imshow('img',img)
cv2.waitKey(0)