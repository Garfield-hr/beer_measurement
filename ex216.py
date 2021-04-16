import cv2 as cv
import numpy as np
from imgSeg import dir_str, img_str
from hsvSeg import hsv_seg


def hsv_dialation():
    img = cv.imread(dir_str + img_str)
    img = cv.flip(img, 0)
    cv.imshow('img', img)
    selected_img = hsv_seg(img)

    # kernel = np.ones((5, 5), np.uint8)
    # dialation = cv.dilate(selected_img, kernel)
    # cv.imshow('final', dialation)
    cv.imshow('final', selected_img)
    cv.waitKey(0)


def ege_detection():
    img = cv.imread(dir_str + img_str)
    img = cv.flip(img, 0)
    cv.imshow('img', img)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    blurred_img = cv.GaussianBlur(hsv_img, (7, 7), 0)
    cv.imshow('blurred', blurred_img)
    canny = cv.Canny(blurred_img, 50, 100)
    cv.imshow('edge', canny)
    cv.waitKey(0)


if __name__ == '__main__':
    vc = cv.VideoCapture('/home/hairui/Videos/experiments/317-1.avi')
    if vc.isOpened():
        ret = True
        while ret:
            ret, frame = vc.read()
            img = cv.flip(frame, 0)
            selected = hsv_seg(img)
            cv.imshow('original', img)
            cv.imshow('selected', selected)
            if cv.waitKey(33) == 27:
                break

    cv.destroyAllWindows()
