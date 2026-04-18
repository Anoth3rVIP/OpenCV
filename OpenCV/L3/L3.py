import cv2
import numpy as np

img = cv2.imread('image.png', 1)
kernel = np.ones((7,7),np.uint8)
erdimg = cv2.erode(img, kernel)
cv2.imshow('eroded image', erdimg)

cv2.waitKey(0)
cv2.destroyAllWindows()