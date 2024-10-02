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


image_inBlueGrayed = image[:,:,0]
image_inGreenGrayed = image[:,:,1]
image_inRedGrayed = image[:,:,2]


# image_inBlue  =
# image[:,:,0]=0
# image_inGreen = 
# image[:,:,1]=0
# image_inRed = 
# image[:,:,2]=0

stacked_image = np.hstack((image_inBlueGrayed, image_inGreenGrayed, image_inRedGrayed))
# cv2.imwrite("parrot-stack.png",stacked_image)


created_image =np.zeros((512,512,3))
# Rectagle
rectangle = cv2.rectangle(created_image,pt1=(100,200),pt2=(200,400),color=(255,0,0), thickness=-1)
# pt1=(from left, from above) mean, x , y. y in reverse (from above to bottom)

# thickness=-1 filled
# thickness=3 bordered

# Circle
cv2.circle(created_image,(100,100), radius=30, color= (0,0,255), thickness=10)
cv2.circle(created_image,(200,100), radius=30, color= (0,0,255), thickness=10)
# Line
cv2.line(created_image, pt1=(0,512), pt2=(512,0), color=(255,255,0), thickness=4)

cv2.line(created_image, pt1=(60,160), pt2=(250,160), color=(255,255,0), thickness=4)
# Text
cv2.putText(created_image,text="Hi,Bro", org=(300,300), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255,0,244))
# Triangle



cv2.imshow('window',created_image)
cv2.waitKey(5000) 