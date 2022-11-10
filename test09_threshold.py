#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 阈值算法：二值化算法，把灰度图像分为黑与白，阈值以下为黑色，否则白色
import cv2

gray = cv2.imread("./bookpage.jpg", cv2.IMREAD_GRAYSCALE)
# 最简单的阈值处理是固定一个阈值，如阈值为10，最大灰度255
# threshold返回结果第一个值就是输入的thresh值（阈值），第二个就是处理后的图像
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# 当无法确定具体阈值时，可以采用自适应阈值算法，即把图片分成很多区域，每个区域独立计算阈值
# 光照强的部分阈值大，光照弱的部分阈值小
# 设置区域大小为115个像素
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# 一种常用的阈值算法——大津法（Otsu）：不需要人为确定阈值，本质是聚类分析算法
# 在使用Otsu方法时，要把阈值设为0。此时的函数cv2.threshold（）会自动寻找最优阈值，并将该阈值返回
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("gry", gray)
cv2.imshow("binary", binary)
cv2.imshow("adaptive", binary_adaptive)
cv2.imshow("otsu", binary_otsu)
cv2.waitKey()