import cv2 as cv
from imgSeg import MouseInput
import numpy as np


def cup_seg():
    dir_str = '/home/hairui/Pictures/experiment/'
    img_str = 'bad.jpeg'
    img = cv.imread(dir_str + img_str)

    MouseIn = MouseInput(img)
    rect = MouseIn.get_rect()
    x, y, w, h = rect
    print(rect)
    img_roi = img[y:y + h, x:x + w]
    cv.imshow('roi', img_roi)
    cv.waitKey(0)
    str_name = input('Please input the name of this image')
    cv.imwrite('/home/hairui/Pictures/experiment/' + str_name, img_roi)
    cv.destroyAllWindows()


def roi_process():
    dir_str = '/home/hairui/Pictures/experiment/'
    img_str = 'cup.jpeg'
    img = cv.imread(dir_str+img_str)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', img_hsv)
    img_select = cv.inRange(img_hsv, np.array([133, 26, 0]), np.array([180, 69, 77]))
    cv.imshow('selected', img_select)
    cv.waitKey(0)
    str_name = input('Please input the name of this image')
    cv.imwrite('/home/hairui/Pictures/experiment/' + str_name, img_select)
    cv.destroyAllWindows()


if __name__ == '__main__':
    cup_seg()
