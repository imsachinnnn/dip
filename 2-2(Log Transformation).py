import cv2 
import numpy as np 
 
# Load the image 
image1 = cv2.imread('resized_image.jpg', cv2.COLOR_BGR2GRAY) 
image = cv2.imread('resized_image.jpg', cv2.IMREAD_GRAYSCALE)   
 
# Convert the image pixel values to float for computation 
image_float = np.float32(image) 
 
# Apply log transformation 
c = 255 / np.log(1 + np.max(image_float)) 
log_image = c * (np.log(1 + image_float)) 
 
# Convert back to uint8 
log_image = np.uint8(log_image) 
 
# Display the images 
cv2.imshow('Original Color Image', image1) 
cv2.imshow('Gray Scaled Image', image) 
cv2.imshow('Log Transformed Image', log_image) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows()
