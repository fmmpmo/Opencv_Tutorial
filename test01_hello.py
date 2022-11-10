#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import cv2

print(cv2.getVersionString()) # 版本号 4.5.5
image = cv2.imread("./opencv_logo.jpg") # numpy类型
print(image.shape) # (250, 250, 3). 250*250像素，3是RGB彩色通道

cv2.imshow("image", image) # 窗口名，文件名。只有这一行会发现图片一闪而过
cv2.waitKey() # 一直等待键盘输入，在窗口上输入任意键，关闭窗口
