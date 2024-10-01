import numpy as np
import cv2

image = cv2.imread('images/parrot.png')

image_crop = image[0:300,0:400] # height x width

image_resize = cv2.resize(image, (500,200)) # width x height

image_flip = cv2.flip(image, 0) 
# -1 flips it both vertically and horizontally
# 1 flips it horizontally
# 0 flips it vertically
image_rgbToGrayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# image_inBlueGrayed = image[:,:,0]
# image_inGreenGrayed = image[:,:,1]
# image_inRedGrayed = image[:,:,2]


# image_inBlue  =
# image[:,:,0]=0
# image_inGreen = 
image[:,:,1]=0
# image_inRed = 
# image[:,:,2]=0

cv2.imshow('window',image)
cv2.waitKey(5000) 