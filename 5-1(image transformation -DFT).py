# import required libraries
import numpy as np
import cv2
# Load and display an image in grayscale
img = cv2.imread('log-image.png', 0)
cv2.imshow("Input Image", img)
# Perform DFT and shift the result to the center
f = np.fft.fft2(img)
fs = np.fft.fftshift(f)
# Convert the complex values to the magnitude and display the image
lfs = 15 * np.log(1 + np.abs(fs))
cv2.imshow("DFT of the image", np.uint8(lfs))
# Apply inverse Fourier Transform
ishift_img = np.fft.ifftshift(fs)
ifft_img = np.fft.ifft2(ishift_img)
abs_img = np.abs(ifft_img)
# Display the reconstructed image
cv2.imshow("Reconstructed Image",np.uint8(abs_img))
cv2.waitKey(0)
cv2.destroyAllWindows()
