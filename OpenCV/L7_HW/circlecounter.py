import cv2
import numpy as np

image = cv2.imread("alien.jpg")

if image is None:
    print("Image not Found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 2)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1.2, minDist=40, param1=100, param2=30, minRadius=5, maxRadius=100)

output = image.copy()
numOfCircles = 0
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    numOfCircles = len(circles)
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 0, 255), 2)
        cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 255, 0), 2)

print(numOfCircles)

cv2.putText(output, 'Circles Detected:'+str(numOfCircles), (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
display = cv2.resize(output, (900,600))
cv2.imshow('Circle Detection', display)

cv2.waitKey(0)
cv2.destroyAllWindows()
