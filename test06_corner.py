#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 图像特征的提取
import cv2

image = cv2.imread("./opencv_logo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY) # 把彩色图像转换为灰度图

# 获取图像特征点，最多500个，点的质量优于0.1，特征点之间的距离大于10个像素
corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
# 找到特征点之后，把每一个特征点标记出来
for corner in corners:
    x, y = corner.ravel() # 函数ravel()的作用是将二维数组降维成一维数组
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)
    # 可以发现识别出来的特征都是图像的转角，是一种最简单的图像特征

cv2.imshow("corner", image)
cv2.waitKey()