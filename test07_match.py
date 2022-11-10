#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 特征提取：模板匹配扑克牌上的菱形
import cv2
import numpy as np

image = cv2.imread("./poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY) # 转为灰度图

# 选取区域
template = gray[75:105, 235:265]
# 使用标准相关匹配算法，即把待检测图像和模板都各自标准化再来计算匹配度，这样可以保证匹配结果不受光照强度的影响
# 该匹配算法是对大小敏感的，所以比较小的菱形没有找到，若都找到，可以放大缩小图像，匹配多次
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# 找出匹配系数大于0.9的匹配点
locations = np.where(match >= 0.9)
# 把模板长和宽求出，方便作图
w, h = template.shape[0:2]
# 循环遍历每一个匹配点，在原始图像上画出对应的矩形框
for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey()