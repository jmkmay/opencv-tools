import numpy as np
import cv2

# Documentation: http://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # hsv is hue, sat, value
    # start modifying hue to change the mask
    lower_red = np.array([130, 150,50])
    upper_red = np.array([200,255,150])
    '''
    For converting rgb to hsv:
    dark_red = np.uint8([[[12.22.121]]])
    dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
    '''
    # mask is a binary image that shows where threshold is met
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # apply mask to frame to get filtered result
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # morphology kernel
    kernel = np.ones((10,10), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    #morphology = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    #cv2.imshow('frame',frame)
    #cv2.imshow('result',result)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation',dilation)
    #cv2.imshow('morphology',morphology)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
