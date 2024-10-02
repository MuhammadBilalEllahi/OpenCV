import cv2
import numpy as np


image = cv2.imread('images/parrot.png')

flag=False
ix = -1
iy = -1

def crop(event,x,y,flags,params):
    global flag,ix,iy,image
    
    if event == 1:
        flag=True
        ix = x
        iy = y
    elif event == 0:
        if flag == True:
            image = cv2.imread('images/parrot.png')
            cv2.rectangle(image,pt1=(ix,iy), pt2=(x,y), thickness=1 , color=(0,0,0))
            
            
    elif event == 4:
        flag=False
        curX=x
        curY=y
        cv2.rectangle(image,pt1=(ix,iy), pt2=(x,y), thickness=1 , color=(0,0,0))
        image = image[iy:curY,ix:curX] 
        # cv2.destroyAllWindows()
        cv2.imshow('window',image)
        cv2.waitKey(0)
        # crop(event=event,x=x,y=y,flags=flags,params=params)

cv2.namedWindow('window')
cv2.setMouseCallback('window',crop)

while True:
    cv2.imshow('window',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()