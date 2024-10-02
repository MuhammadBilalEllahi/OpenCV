import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    out.write(frame)
    
    vid = cv2.flip(frame,1)
    image_gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    # image_humanAvatar = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
    
    # print(ret)
    cv2.imshow('webcam',image_gray)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()