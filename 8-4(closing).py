import cv2 as cv
import matplotlib.pyplot as plt
# Load and display the input image
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')
# Create a cross structuring element (kernel) of size 5×5 
kernel = cv.getStructuringElement(cv.MORPH_CROSS,(5,5)) 
print(kernel)
# Apply dilation followed by erosion with the structuring element
dilation = cv.dilate(img,kernel,iterations = 1)
closing = cv.erode(dilation,kernel,iterations = 1)
# Display the closing image
plt.subplot(1, 2, 2),plt.imshow(closing, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Closed Image')
