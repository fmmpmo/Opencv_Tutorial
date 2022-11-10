#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 图像的梯度算法与边缘检测

# 图像梯度指图像的明暗变化，比如可以计算图像沿水平和垂直方向上的明暗变化，再取这两个变换的平方和，就得到了梯度
import cv2

# 梯度算法接受的是灰度图
gray = cv2.imread("./opencv_logo.jpg", cv2.IMREAD_GRAYSCALE) # 直接读取灰度图
# 拉普拉斯算子，大致对应图像的二阶导数
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
# canny边缘检测算法，使用梯度区间来定义边缘：比如100~200，如果某个像素的梯度>200,则可以确定是边缘
# 若<100则为非边缘，若100<px<=200则待定,如果和某个已知的像素边缘连在一起，则也判断为边缘
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian) # 均一的背景颜色变为黑色，有明暗变化的部分，比比如边缘部分变成了白色
cv2.imshow("canny", canny)# 边缘被完美检测出来
cv2.waitKey()