import cv2

img = cv2.imread('image.png')

brdimg = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_TRANSPARENT, value=(255,0,0))
cv2.imshow('brdrdimg', brdimg)
cv2.waitKey(0)

cv2.destroyAllWindows()