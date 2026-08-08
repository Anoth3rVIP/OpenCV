import cv2
import numpy as np
import time

print("OpenCV Version:",cv2.__version__)

capture_vid = cv2.VideoCapture("Video.mp4")

time.sleep(1)

width = int(capture_vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture_vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture_vid.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(
    "Invisible_Cloak_Output.avi",
    fourcc,
    fps,
    (width, height)
)

bakground = None

for i in range(60):
    ret, background = capture_vid.read()
    if not ret:
        continue
    
background = np.flip(background, axis = 1)
delay = 1
frame_count = 0

while capture_vid.isOpened():
    ret, img = capture_vid.read()
    
    if not ret:
        break
    
    frame_count += 1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    
    lower_red2 = np.array([160,120,70])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = mask1 + mask2
    kernel = np.ones((3,3), np.uint8)
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel)
    mask_inv = cv2.bitwise_not(mask)
    
    res1 = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )
    
    res2 = cv2.bitwise_and(
        img,
        img,
        mask=mask_inv
    )
    
    final_output = cv2.add(res1, res2)