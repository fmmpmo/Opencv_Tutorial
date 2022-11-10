#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 绘制直线，矩形，圆形
# opencv的图像数据实际上是numpy数组数据结构，所以可以使用numpy创建黑色画布
import cv2
import numpy as np

image = np.zeros([300, 300, 3], dtype=np.uint8)

# 要绘制的图像，线段的起点，线段的终点，线段的RGB颜色（这里是蓝色）， 线段的粗细是2个像素
cv2.line(image, (100, 200), (250, 250), (250, 0, 0), 2)
# 要绘制的图像，矩形的第一个顶点（左上角），矩形的对角顶点（右下角），颜色（这里是绿色），粗细为2像素
cv2.rectangle(image, (30, 100), (60, 150), (0, 255, 0), 2)
# 要绘制的图像，圆心坐标，半径，颜色，粗细
cv2.circle(image, (150, 100), 20, (0, 0, 255), 2)
# 要绘制的图像，字符串内容，起始位置，字体序号（默认0），缩放系数，颜色（白色），粗细，线条类型1（实线）
cv2.putText(image, "hello world", (100, 50), 0, 1, (255, 255, 255), 2, 1)

cv2.imshow("image", image)
cv2.waitKey()