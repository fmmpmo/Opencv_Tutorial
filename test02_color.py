#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 对于opencv来说，存储一张彩色图片等同于存储三张灰度图。它们被存储在opencv的第三个维度上，
# 灰度范围是0-255，opencv对颜色的存储是BGR，即蓝绿红。当显示器需要渲染这张图片时，
# 计算机会依次取出这三张灰度图，再把它们分别投影到显示器对应的三个LED芯片上
import cv2

image = cv2.imread("./opencv_logo.jpg")

cv2.imshow("blue", image[:, :, 0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])

# 彩色图像的灰度变换算法：平方和加权平均
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
cv2.imshow("gray", gray) # bgr三原色的平均，


cv2.waitKey()