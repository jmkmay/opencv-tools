import numpy as np
import cv2

img = cv2.imread('basketball.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)

# ROI stands for Region of image
img[100:150, 100:150] = [255,255,255]

basket_ball = img[37:111, 107:194]
img[0:74, 0:87] = basket_ball

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.DestroyAllWindows