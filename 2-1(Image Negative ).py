import cv2 
# Load the image 
image = cv2.imread('lena.bmp') 
# Check the datatype of the image and find the intensity resolution 
print(image.dtype) 
# Subtract the image from the max value (calculated from dtype) 
img_neg = 255 – image 
# Display both original and negative image 
cv2.imshow('Input Image', image) 
cv2.imshow('Negative', img_neg) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
