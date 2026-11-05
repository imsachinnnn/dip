import cv2
import numpy as np
# Read input image as grayscale
img = cv2.imread('resized_image.jpg', 0)
# Convert the grayscale to float32
imf = np.float32(img) # float conversion
# Find Discrete Cosine Transform
dst = cv2.dct(imf, cv2.DCT_INVERSE)
# Apply inverse Discrete Cosine Transform
img1 = cv2.idct(dst)
# Convert to uint8
img1 = np.uint8(img)
# Display the images
cv2.imshow("DCT of the Input Image", dst)
cv2.waitKey(0)
cv2.imshow("Reconstructed image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
