#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 图像的裁剪
import cv2

image = cv2.imread("./opencv_logo.jpg")
crop = image[10:170, 40:200] # 取出图片的一部分

cv2.imshow("crop", crop)
cv2.waitKey()