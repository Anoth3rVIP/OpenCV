import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')

#Triangle
points = np.array([[250, 100], [100, 400], [400, 400]])
cv2.fillPoly(img, [points], (0, 255, 255))


#Penatgon
points = np.array([[250, 80], [100, 200], [150, 400], [350, 400], [400, 200]])
cv2.fillPoly(img, [points], (255, 255, 0))

#Diamond
points = np.array([[250, 100], [100, 250], [250, 400], [400, 250]])
cv2.fillPoly(img, [points], (0, 255, 0))

#Arrow
cv2.arrowedLine(img, (50,250), (450,250), (255, 0, 0), 3)

cv2.imshow('Extshps', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
