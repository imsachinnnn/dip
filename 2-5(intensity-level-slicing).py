import cv2 
import numpy as np 
 
# Load the image 
img = cv2.imread('log-image.png',0) 
 
# Find width and height of image 
row, column = img.shape 
 
# Create a zeros array to store the sliced image 
img1 = np.zeros((row,column),dtype = 'uint8') 
 
# Specify the min and max range 
min_range = 30 
max_range = 90 
 
# Loop over the input image and if pixel value lies in  
desired range set it to 170 otherwise set it to 50. 
 
for i in range(row): 
    for j in range(column): 
        if img[i,j]>min_range and img[i,j]<max_range: 
            img1[i,j] = 170 
        else: 
            img1[i,j] = 50 
 
# Display the images 
cv2.imshow('Input image', img) 
cv2.imshow('Sliced image', img1) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
