import numpy as np
import cv2

img = cv2.imread('basketball.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255, 255, 255), 15)
cv2.rectangle(img, (15,25), (200,150), (255,0,0), 5)
cv2.circle(img, (100,63), 55, (0,255,0), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10],[11,45]], np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
# Where, text message, location, font, size of font, color, thickness, anti-
cv2.putText(img,'OpenCV Tuts!', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
