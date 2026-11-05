import cv2
import numpy as np
# Load the input image
original_image=cv2.imread("lena.bmp")
cv2.imshow('original image',original_image)
cv2.waitKey(0)
# Create a sharpening kernel
sharpen_filter=np.array([[-1,-1,-1],
 [-1,9,-1],
 [-1,-1,-1]])
# Apply kernel to the input image to get the sharpened image
sharp_image=cv2.filter2D(original_image,-1,sharpen_filter)
# Display the sharpened image
cv2.imshow('Sharpened image',sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
