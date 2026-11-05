import cv2 as cv
from matplotlib import pyplot as plt
# Load and display the input image
img = cv.imread('1.png', cv.IMREAD_GRAYSCALE)
cv.imshow('Input Image',img)
# Find and display the histogram of the input image
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.show()
# Equalize the input image and display the equalized image
equ = cv.equalizeHist(img)
cv.imshow('Equalized',equ)
# Display the histogram of the equalized image
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
