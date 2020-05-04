import numpy as np
import cv2

image = cv2.imread('/home/saket/vision/image-matting/indexnet_matting/examples/tmp/output_file_name_gray.png', 0)
classes = np.unique(image)
print(classes)

for cls in classes:
    if cls == 0:
        continue
    im = np.zeros_like(image)
    class_mask = image == cls
    im[class_mask] = 255
    im = cv2.resize(im, (1920, 1080), cv2.INTER_NEAREST)

    r, c = im.shape
    offset = 5
    if cls == 3:
        offset = 10

    m1 = im[offset:, :] != im[:r-offset, :]
    m2 = im[:r-offset, :] != im[offset:, :]
    m3 = im[:, offset:] != im[:, :c-offset]
    m4 = im[:, :c-offset] != im[:, offset:]

    im[offset:, :][m1] = 128
    im[:r-offset, :][m2] = 128
    im[:, offset:][m3] = 128
    im[:, :c-offset][m4] = 128

    cv2.imwrite(f'{cls}_tm3.png', im)
    print(im.shape)

