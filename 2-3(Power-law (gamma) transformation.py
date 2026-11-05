import numpy as np 
import cv2 
 
# Load the image 
img = cv2.imread('gamma.jpg') 
 
# Apply Gamma=0.4 on the normalised image  
# then multiply by the constant (For 8 bit, c=255) 
gamma_point_four = np.array(255*(img/255)**0.4,dtype='uint8') 
 
# Apply Gamma=1.2  
gamma_one_point_two = np.array(255*(img/255)**1.2,dtype='uint8') 
 
# Similarly, Apply Gamma=2.4  
gamma_two_point_four = np.array(255*(img/255)**2.4,dtype='uint8') 
 
# Display the images in subplots 
img3 = cv2.hconcat([img,gamma_point_four]) 
img4 = cv2.hconcat([gamma_one_point_two,gamma_two_point_four]) 
 
cv2.imshow('a1',img3) 
cv2.imshow('a2',img4) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows()
