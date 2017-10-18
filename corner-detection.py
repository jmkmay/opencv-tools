import cv2
import numpy as np

src = cv2.imread('corner-shapes.jpg')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
src_gray = np.float32(src_gray)

corners = cv2.goodFeaturesToTrack(src_gray,200,0.01,10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(src, (x,y), 3, 255, -1)

cv2.imshow('corners', src)
cv2.waitKey(0)
cv2.destroyAllWindows
