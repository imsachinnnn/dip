import cv2
import numpy as np
#-----------------------------Load and display the image ----------------#
image = cv2.imread('coins_01.jpg')
plt.imshow(image)
#------------------- Change the color to RGB from BGR---------------------#
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
#-----Reshaping the image into a 2D array of pixels and 3 color values (RGB) 
pixel_vals = image.reshape((-1,3)) 
#------Convert to float type only for supporting cv2.kmean----------------#
pixel_vals = np.float32(pixel_vals)
#-----------------------Set the criteria for clustering-------------------#
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85) 
 
#-------------------Choose number of clusters-----------------------------#
k = int(input('Enter the number of clusters (k)'))
#-------------------Apply k-means clustering -----------------------------#
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, 
cv2.KMEANS_RANDOM_CENTERS) 
 
#-------------------Convert data into 8-bit values ----------------------#
centers = np.uint8(centers) 
segmented_data = centers[labels.flatten()] 
#----------- Reshape data into the original image dimensions ------------#
segmented_image = segmented_data.reshape((image.shape)) 
 
plt.imshow(segmented_image)
