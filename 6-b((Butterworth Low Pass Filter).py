import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
# Function to find the distance 
def distance(point1,point2):
 return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
# Function to create Butterworth low pass filter 
def butterworthLP(D0,n,imgShape):
 base = np.zeros(imgShape[:2])
 rows, cols = imgShape[:2]
 center = (rows/2,cols/2)
 for x in range(cols):
 for y in range(rows):
 base[y,x] = 1/(1+((distance((y,x),center)/D0)**(2*n)))
 return base
# Read and show the input image in grayscale mode 
img = cv2.imread('sample2.jpeg',0) 
plt.imshow(img, cmap='gray') 
plt.xticks([]), plt.yticks([]) 
plt.show()
# Compute and display 2D Discrete Fourier Transform of the input image
f = np.fft.fft2(img) 
mag = 20*np.log(np.abs(f))
plt.imshow(mag, cmap = 'gray') 
plt.title('Magnitude Spectrum') 
plt.xticks([]), plt.yticks([])
plt.show()
# Shift the Fourier spectrum to the centre and plot it
fshift = np.fft.fftshift(f)
mag = 20*np.log(np.abs(fshift)) 
plt.imshow(mag, cmap = 'gray')
plt.title('Centered Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
fig, ax = plt.subplots()
im = ax.imshow(np.abs(butterworthLP(30,2,img.shape)), cmap='gray')
ax.set_title('Butterworth Low Pass Filter of Diameter 30 px')
ax.set_xticks([])
ax.set_yticks([])
# Filter the input image with the BLPF of diameter 30 and display the 
# filtered image
fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(fshift * butterworthLP
(30,2,img.shape))), cmap='gray')
ax.set_title('Filtered Image in Frequency Domain')
ax.set_xticks([])
ax.set_yticks([])
# Shift the filtered image from the centre to its original position 
#and display it
fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifftshift(fshift * butterworthLP
(30,2,img.shape)))), cmap='gray')
ax.set_title('Filtered Image inverse fft shifted')
ax.set_xticks([])
ax.set_yticks([])
# Apply 2D Inverse DFT on the filtered image and display it in the 
spatial domain
fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * 
butterworthLP (30,2,img.shape))))), cmap='gray')
ax.set_title('Final Filtered Image In Spatial Domain')
ax.set_xticks([])
ax.set_yticks([])
cv2.waitKey(0)
cv2.destroyAllWindows()
