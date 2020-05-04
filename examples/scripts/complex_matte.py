import numpy as np
import cv2

image = cv2.imread('/home/saket/vision/image-matting/indexnet_matting/examples/tmp/output_file_name_gray.png', 0)
hair = cv2.imread('/home/saket/vision/image-matting/indexnet_matting/examples/tmp/tm3.jpg', 0)
classes = np.unique(image)
print(classes)
image = cv2.resize(image, (1920, 1080))
print(image.shape)
print(hair.shape)

image[image == 2] = 0
image[image > 0] = 255
image[hair > 0] = hair[hair > 0]

cv2.imwrite('output_file_name_gray_matte.png', image)
