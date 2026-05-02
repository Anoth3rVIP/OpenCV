import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype='uint8') * 255

#  [start](x, y), [end] (x, y), [clr] (B, G, R), [thickness] (number)
#[thickness] if < 0 (fills in shape), if <= 0 (line thickness) {line has to be < 0}
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(img, (50, 100), (450, 250), (0, 255, 0), 0)

#  [center] (x, y), [radius] num, ...same as default shape
cv2.circle(img, (100, 350), 50, (0, 0, 255), -1)

cv2.imshow('dwdemo', img)

cv2.waitKey(0)
cv2.destroyAllWindows()