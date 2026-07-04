import cv2
import numpy as np

image = cv2.imread("blobs.jpg")

if image is None:
    print("Image not Found!")
    exit()
    
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY_INV)

params = cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 255

params.filterByArea = True

params.minArea = 2000
params.maxArea = 200000

params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(thresh)

output = image.copy()
output = cv2.drawKeypoints(
    output, keypoints, None,
    (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)
numOfBlobs = len(keypoints)
print(numOfBlobs)

cv2.putText(output, 'Blobs Detected:'+str(numOfBlobs), (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
display = cv2.resize(output, (900,600))
cv2.imshow('Blob Detection', display)

cv2.waitKey(0)
cv2.destroyAllWindows()