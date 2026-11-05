import cv2
# Read the input image
img = cv2.imread('deer.png')
# Get the Averaging filter mask size from the user
k=int(input('Enter the size of the kernel: '))
# Filter the source image using cv2.boxfilter()
blur = cv2.boxFilter(img,-1,(k,k), normalize = True)
# Filter the source image using cv2.blur()
blur1 = cv2.blur(img,(k,k))
# Display both blurred images and compare the results
cv2.imshow('blur',blur)
cv2.imshow('blur1',blur1)
cv2.waitKey(0)
cv2.destroyAllWindows()
