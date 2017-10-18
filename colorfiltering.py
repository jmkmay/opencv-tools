import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # hsv is hue, sat, value
    # start modifying hue to change the mask
    lower_red = np.array([130  , 150,50])
    upper_red = np.array([255,255,255])
    '''
    For converting rgb to hsv:
    dark_red = np.uint8([[[12.22.121]]])
    dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
    '''
    # mask is a binary image that shows where threshold is met
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # apply mask to frame to get filtered result
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # averaged blur effect
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(result, -1, kernel)

    # gaussian blur
    gauss = cv2.GaussianBlur(result, (15,15), 0)

    # median blur
    median = cv2.medianBlur(result,15)

    # bilateral blur
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)


    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('smoothed',smoothed)
    # cv2.imshow('gauss',guass)
    cv2.imshow('bilateral',bilateral)
    cv2.imshow('result',result)
    #cv2.imshow('median',median)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
