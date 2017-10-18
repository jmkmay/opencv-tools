import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus1 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 75, 1)
gaus2 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 175, 1)
# retval2, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_OTSU)

template = cv2.imread('t.png')
w, h = template.shape[::-1]

result = cv2.matchTemplate(gaus2, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(gaus2, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', result)
#cv2.imshow('original',img)
#cv2.imshow('threshold',threshold)
#cv2.imshow('threshold2',threshold2)
#cv2.imshow('gauss',gaus1)
cv2.imshow('guass2',gaus2)
#cv2.imshow('otsu',otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
