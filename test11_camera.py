#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 使用opencv调用电脑中的摄像头
import cv2

# 获取摄像头的指针，需要传入摄像头的序号（设备管理器 -> 摄像头）,传入0表示内置摄像头，若视频地址，则为播放视频
capture = cv2.VideoCapture(0)

# 对于摄像头的采集是连续不断的，即循环读取每一帧的画面，由于不确定循环多少次，可以先做死循环
while True:
    # 读取摄像头中的画面，ret是分布值bool，如果读取帧正确则为True，文件结尾为False，fram就是每一帧的图像，为一个三维矩阵
    ret, frame = capture.read()
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1) # 等待键盘1ms
    if key != -1: # 如果输入任意键，则返回值不为-1.即按键跳出循环
        break

capture.release() # 释放capture指针