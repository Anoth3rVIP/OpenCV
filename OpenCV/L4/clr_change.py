import cv2
import numpy as np

#       .full (bg fill), [size] (x , y, color channel), [clr] (B, G, R)
img = np.full((500, 500, 3), (0, 255, 255), dtype='uint8')
#                            (color = yellow?)

# Same shapes as L4 definitions in L4
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(img, (50, 100), (450, 250), (0, 255, 0), 0)
cv2.circle(img, (100, 350), 50, (0, 0, 255), -1)

cv2.imshow('dwdemo', img)

cv2.waitKey(0)
cv2.destroyAllWindows()