import numpy as np
import cv2
# Read the input image
img_src = cv2.imread('noisy.jpeg')
# Select and enter the kernel size of the median filter
k=int(input('Enter the size of the kernel: '))
 
# Apply median filter
img_rst=cv2.medianBlur(img_src, k)
# Save the filtered image
cv2.imwrite('clear.jpg',img_rst)
cv2.waitKey(0)
cv2.destroyAllWindows()
