import numpy as np
import cv2

image = cv2.imread('images/parrot.png')

cv2.imshow('window',image)
cv2.waitKey(0) 