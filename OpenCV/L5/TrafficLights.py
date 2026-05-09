import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype='uint8') * 255

#Text
img = cv2.putText(img, 'TRAFFIC LIGHT', (130, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

#Base
cv2.rectangle(img, (175, 50), (325, 350), (128, 128, 128), -1)
#Support
cv2.rectangle(img, (240, 350), (260, 450), (128, 128, 128), -1)

#Lights
cv2.circle(img, (250, 100), 40, (0, 255, 0), -1)
cv2.circle(img, (250, 200), 40, (0, 255, 255), -1)
cv2.circle(img, (250, 300), 40, (0, 0, 255), -1)

cv2.imshow('tldemo', img)

cv2.waitKey(0)
cv2.destroyAllWindows()