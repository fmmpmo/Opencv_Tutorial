#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 图像形态学之腐蚀和膨胀，二者可以交替使用
import cv2
import numpy as np

gray = cv2.imread("./opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

# 基于二值化图像，所以要设置阈值，这里使用反阈值（原始图像背景是白色的，需要把背景变为黑色，图像变为白色）
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
# 使用kernel来腐蚀图像
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(binary, kernel)

# 与腐蚀对应的是膨胀 ,这里采用同一个内核kernel
dilation = cv2.dilate(binary, kernel)

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion) # 发现图像变瘦了，像把边缘腐蚀掉一般
cv2.imshow("dilation", dilation) # 变胖
cv2.waitKey()