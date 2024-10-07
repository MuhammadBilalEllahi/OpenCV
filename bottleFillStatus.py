import cv2
import numpy as np
import matplotlib.pyplot as plt

bottle_image_path = 'images/WhatsApp Image 2024-10-07 at 3.23.09 PM.jpeg'
# bottle_image_path = 'images/dark-drink-gray-bg.png'
imgREad = cv2.imread(bottle_image_path)

gray = cv2.cvtColor(imgREad, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image",gray)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# cv2.imshow("Blurred Image",blur)
edges = cv2.Canny(blur, 0, 250)
# cv2.imshow("Edged Image",edges)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i,contour in enumerate(contours):

    x, y, w, h = cv2.boundingRect(contour)
    
    # print(f"Cont Info: x={x}, y={y}, w={w}, h={h}")
    bottle_region = imgREad[y:y+h, x:x+w]
    

    hsv_bottle = cv2.cvtColor(bottle_region, cv2.COLOR_BGR2HSV)
    
    
    
    # The below code is to show ech cotour
    
    # plt.subplot(len(contours), 2, i*2+1)
    # plt.imshow(cv2.cvtColor(bottle_region, cv2.COLOR_BGR2RGB))
    # plt.title(f" Contour {i+1}")
    # plt.axis('off')

    # plt.subplot(len(contours), 2, i*2+2)
    # plt.imshow(hsv_bottle)
    # plt.title(f"HSV {i+1}")
    # plt.axis('off')

    lower_liquid = np.array([50, 40, 10])  
    upper_liquid = np.array([255, 255, 255])
    

    liquid_masking = cv2.inRange(hsv_bottle, lower_liquid, upper_liquid)
    

    kernel = np.ones((5,5), np.uint8)
    liquid_masking = cv2.morphologyEx(liquid_masking, cv2.MORPH_CLOSE, kernel)
    

    _liquid_contours, _ = cv2.findContours(liquid_masking, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if _liquid_contours:
    
        most_liquid_contour = max(_liquid_contours, key=cv2.contourArea)
        
    
        lx, ly, lwidth, lheight = cv2.boundingRect(most_liquid_contour)
        # print(f"Liq Info: lx={lx}, ly={ly}, lwidth={lwidth}, lheight={lheight}")
    
        total_height = bottle_region.shape[0]
        
        fill_height = total_height - ly
        
        _ratio_of_filling = fill_height / total_height
        
    
        cv2.rectangle(imgREad, (x + lx, y + ly), (x + lx + lwidth, y + ly + lheight), (0, 255, 0), 2)
        
    
        cv2.putText(imgREad, f"Fill: {_ratio_of_filling*100:.2f}%", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (60, 0, 0), 1)

plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(imgREad, cv2.COLOR_BGR2RGB))

plt.title('Bottle Water Level Fill Status')
plt.axis('off')

plt.show()
# plt.close(20)
