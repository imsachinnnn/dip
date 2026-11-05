import cv2
import matplotlib.pyplot as plt
# Load the image
img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
# Finding the histogram using Matplotlib
plt.hist(img.ravel(),256,[0,256]); 
# Display the histogram
cv2.imshow('Input image', img)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Histogram using Matplotlib')
plt.show()
# Finding the histogram using OpenCV
histr = cv2.calcHist([img],[0],None,[256],[0,256])
# Display the histogram
p1=plt.plot(histr)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Histogram using OpenCV')
plt.show()
# Finding the normalized histogram using OpenCV
cv2.normalize(histr, histr, 0, 1, cv2.NORM_MINMAX)
plt.plot(histr)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Normalized Histogram using OpenCV')
cv2.waitKey(0)
cv2.destroyAllWindows()
