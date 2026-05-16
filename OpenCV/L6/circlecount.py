import cv2
import numpy as np

image = cv2.imread("circles.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not Found!")
    exit()
    
_, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)

thresh - cv2.GaussianBlur(thresh, (5, 5), 0)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10
params.maxThreshold = 200

params.filterByColor = True
params.blobColor = 255

params.filterByArea = True