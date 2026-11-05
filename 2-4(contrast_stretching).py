import cv2 
import numpy as np 
 
# Read the image 
img = cv2.imread('lena.bmp',0) 
 
# Create zeros array to store the stretched image 
minmax_img = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8') 
 
# Loop over the image and apply Min-Max formulae 
for i in range(img.shape[0]): 
    for j in range(img.shape[1]): 
        minmax_img[i,j] = 255*(img[i,j]-np.min(img))/(np.max(img)-np.min(img)) 
 
# Display both the images 
cv2.imshow('Original Image',img) 
cv2.imshow('Contrast Stretched',minmax_img) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows()
