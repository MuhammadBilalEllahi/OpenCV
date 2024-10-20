# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# my_image = cv2.imread('bilalellahi_skin_image.jpeg')

# my_image_in_YCbCr = cv2.cvtColor(my_image, cv2.COLOR_BGR2YCrCb)

# Y_brightness, Cred, Cblue = cv2.split(my_image_in_YCbCr)

# lowerValueOfCred = 133
# upperValueOfCred= 173
# lowerValueOfCblue = 77
# upperValueOfCblue = 127

# skin_mask = np.logical_and(Cblue >= lowerValueOfCblue, Cblue <= upperValueOfCblue) & np.logical_and(Cred >= lowerValueOfCred, Cred <= upperValueOfCred)

# segmented_image = np.zeros_like(my_image)
# segmented_image[skin_mask] = my_image[skin_mask]


# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB))
# plt.title('Full Image')

# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
# plt.title('Segmented Skin')

# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

my_image = cv2.imread('all_skin_image.jpeg')

my_image_in_YCbCr = cv2.cvtColor(my_image, cv2.COLOR_BGR2YCrCb)

Y_brightness, Cred, Cblue = cv2.split(my_image_in_YCbCr)

lowerValueOfCred = 130
upperValueOfCred = 180


lowerValueOfCblue = 70
upperValueOfCblue = 120

masked_skin = np.logical_and(Cblue >= lowerValueOfCblue, Cblue <= upperValueOfCblue) & np.logical_and(Cred >= lowerValueOfCred, Cred <= upperValueOfCred)

masked_skin = masked_skin.astype(np.uint8) * 255

kernel_of_7x7 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)) # 7x7 removes mmore noise tahn 5x5


masked_skin = cv2.morphologyEx(masked_skin, cv2.MORPH_OPEN, kernel_of_7x7) 

masked_skin = cv2.morphologyEx(masked_skin, cv2.MORPH_CLOSE, kernel_of_7x7) 

segmented_image = cv2.bitwise_and(my_image, my_image, mask=masked_skin)

plt.figure(figsize=(5,10))
plt.subplot(2, 1, 1)
plt.imshow(cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB))

plt.title('Full Image')

plt.subplot(2, 1, 2)

plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmented Skin with Noise Reduction')


plt.show()
