import cv2 as cv
import numpy as np
from imgSeg import dir_str, img_str
from hsvSeg import hsv_seg

img = cv.imread(dir_str+img_str)
img = cv.flip(img, 0)
selected_img = hsv_seg(img)
selected_img_row = np.sum(selected_img, axis=1)
best_seg = 0
max_diff = 0
num_rows = len(selected_img_row)
for ind, val in enumerate(selected_img_row):
    if ind == 0: continue
    diff = sum(selected_img_row[ind:])/(num_rows - ind) - sum(selected_img_row[:ind])/ind
    if diff > max_diff:
        max_diff = diff
        best_seg = ind

cv.line(img, (0, best_seg), (img.shape[1], best_seg), (0, 0, 255), 1, 8)
cv.imshow('img', img)
cv.imshow('binary', selected_img)
cv.waitKey(0)