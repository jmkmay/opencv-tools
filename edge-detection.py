import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    #laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    #sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, ksize=1)
    #sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1, ksize=1)
    src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(src_gray, (3,3))
    edges = cv2.Canny(blur, 30, 30)



    cv2.imshow('original',frame)
    #cv2.imshow('grayscale',blur)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
