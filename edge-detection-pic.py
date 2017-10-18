import numpy as np
import cv2

cap = cv2.VideoCapture(0)

src = cv2.imread('highres3.jpg')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(src_gray, (3,3))
edges1 = cv2.Canny(blur, 60, 60)
edges2 = cv2.Canny(src_gray, 60,60)

cv2.imshow('grayscale', src_gray)
cv2.imshow('blur', blur)
cv2.imshow('edge detection1', edges1)
cv2.imshow('edge detection2', edges2)


cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
