import cv2 as cv
import matplotlib.pyplot as plt
# Load and display the input image
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')
# Create an elliptical structuring element (kernel) of size 5×5 
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) 
print(kernel)
# Dilate the input image with the structuring element
dilation = cv.dilate(img,kernel,iterations = 1) 
# Display the dilated image
plt.subplot(1, 2, 2),plt.imshow(dilation, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Dilated Image')
