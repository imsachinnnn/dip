import pywt
import cv2
from matplotlib import pyplot as plt
# Read the input image
image = cv2.imread('resized_image.jpg', 0)
# Find the wavelet coefficients
coeffs = pywt.dwt2(image, 'bior1.3')
cA, (cH, cV, cD) = coeffs
# Plot the images
plt.subplot(121), plt.imshow(cA, cmap='gray')
plt.title('Approximation Coefficient'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cH, cmap='gray')
plt.title('Horizontal Detail Coefficient'), plt.xticks([]), 
plt.yticks([])
plt.show()
# Apply IDWT to reconstruct the input image
img_recons = pywt.idwt2(coeffs, 'bior1.3')
# Show the resulting image after reconstruction
plt.imshow(img_recons, cmap='gray')
plt.title('Reconstructed Image'), plt.xticks([]), plt.yticks([])
plt.show()
cv.waitKey(0)
