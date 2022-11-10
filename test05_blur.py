#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 均值滤波处理图像噪点
import cv2

image = cv2.imread("./plane.jpg")

# 高斯滤波器，高斯内核设为5个像素，sigMax设为0（也就是sigma由内核大小来决定）
gauss = cv2.GaussianBlur(image, (5, 5), 0)
# 中值滤波器，内核为5个像素
median = cv2.medianBlur(image, 5) # 只有两个参数

cv2.imshow("image", image)
cv2.imshow("gauss", gauss) # 噪点减少了，但也损失了图片细节
cv2.imshow("median", median) # 噪点进一步减少
cv2.waitKey()