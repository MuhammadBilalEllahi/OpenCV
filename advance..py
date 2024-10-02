import numpy as np
import cv2

img = np.zeros((512,512,3))


def draw(event,x,y,flags,params):
    # print(event)
    # event 1 is mouse downclick 
    # event 4 is mouse upclick 
    # if(event==0): #mouse move
    #     cv2.circle(img,center=(x,y),radius=1, thickness=1 , color=(255,255,0))
    if(event==1): 
        cv2.circle(img,center=(x,y),radius=1, thickness=1 , color=(255,255,0))

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)


while True: 
    cv2.imshow('window',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    
    
    
