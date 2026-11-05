import cv2 
import numpy as np 
 
# Read the input image 
img_noisy1 = cv2.imread('noisy3.png', 0) 
 
# Obtain the number of rows and columns of the image 
m, n = img_noisy1.shape 
img_new1 = np.zeros([m, n]) 
# For every pixel in the input image, find the median of the pixels 
# and replace the center pixel with the median 
for i in range(1, m-1): 
 for j in range(1, n-1): 
 temp = [img_noisy1[i-1, j-1], 
 img_noisy1[i-1, j], 
 img_noisy1[i-1, j + 1], 
 img_noisy1[i, j-1], 
 img_noisy1[i, j], 
 img_noisy1[i, j + 1], 
 img_noisy1[i + 1, j-1], 
 img_noisy1[i + 1, j], 
 img_noisy1[i + 1, j + 1]] 
 
 temp = sorted(temp) 
 img_new1[i, j]= temp[4] 
 
img_new1 = img_new1.astype(np.uint8) 
# Store the filtered image
cv2.imwrite('new_median_filtered.png', img_new1) 
cv.waitKey(0)
cv.destroyAllWindows()
