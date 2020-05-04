import numpy as np
import cv2
import sys

SEGMENTATION_DIR = '../segmentations'
TRIMAP_DIR = '../trimaps'
offset = []

def get_tm(segmentation_name):
    '''
    Generates trimaps from a segmentation op.

    Args ::
        segmentation_name -- string | contains the name of the segmented image
    '''
    segmentation  = cv2.imread(os.path.join(SEGMENTATION_DIR, segmentation_name), 0)
    trimap = cv2.resize(segmentation, (1920, 1080))
    print(trimap.shape)
    trimap[segmentation > 0] = 255

    r, c = trimap.shape

    m1 = trimap[offset[0]:, :] != trimap[:r-offset[0], :]
    m2 = trimap[:r-offset[1], :] != trimap[offset[1]:, :]
    m3 = trimap[:, offset[2]:] != trimap[:, :c-offset[2]]
    m4 = trimap[:, :c-offset[3]] != trimap[:, offset[3]:]

    trimap[offset[0]:, :][m1] = 128
    trimap[:r-offset[1], :][m2] = 128
    trimap[:, offset[2]:][m3] = 128
    trimap[:, :c-offset[3]][m4] = 128

    cv2.imwrite(os.path.join(TRIMAP_DIR, segmentation_name), trimap)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        offset = [10, 10, 10, 10]
    else:
        offet[0] = int(sys.argv[1])
        offet[1] = int(sys.argv[2])
        offet[2] = int(sys.argv[3])
        offet[3] = int(sys.argv[4])

    for segmentation_name in os.listdir(SEGMENTATION_DIR):
        get_tm(segmentation_name)

