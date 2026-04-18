import cv2
import numpy as np

img = cv2.imread('image.png', 1)
cv2.imshow('orgimage', img)

gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('gauBlur', gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img, 5)
cv2.imshow('medBlur', median)
cv2.waitKey(0)

biltrl = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bltrlBlur', biltrl)
cv2.waitKey(0)

cv2.destroyAllWindows()