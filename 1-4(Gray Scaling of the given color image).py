import cv2 
image = cv2.imread('sample1.jpg') 
 
# changing the color space 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
 
# showing the resultant image 
cv2.imshow('Original Image', image) 
cv2.imshow('Grayscale Image', gray_image) 
 
cv2.waitKey() 
cv2.destroyAllWindows() 
