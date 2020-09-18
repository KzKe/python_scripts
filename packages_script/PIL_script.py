#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :PIL_script.py
# @Time      :2020/9/18 11:35 上午
# @Author    :Kangke

'''
https://blog.csdn.net/Li_qf/article/details/84925027
'''

from PIL import Image

# 从路径打开
img = Image.open('01.jpg')

## 从文件流读取
f = open('01.jpg', 'rb')
img = Image.open(f) # 不要使用 f.close() 关闭文件，否则会报错, Image会自己调用关闭

### 从二进制流(BytesIO)读取
import os
with open('01.jpg', 'rb') as f:
	img = Image.open(io.BytesIO(f.read()))

# 从numpy数组中读取
import numpy as np
imgarray = np.zeros((200, 200), dtype='uint8') # dtype要指定，否则可能会与预想的结果不一致
imgarray[:100, :100] = 0 # 左上块
imgarray[:100, 100:] = 100 # 右上块
imgarray[100:, 100:] = 150 # 右下块
imgarray[100:, :100] = 200 # 左下块
img = Image.fromarray(imgarray) # 生成一张灰度图片,具体图片可以看下面的图片

## 从opencv图片读取，其实等同与从numpy数组中读取，因为opencv图片保存在numpy数组内
import cv2
# import numpy as np
imgarray = cv2.imread('01.jpg', 0) # 以灰度的方式读取图片
img = Image.fromarray(imgarray)

### 把Image图片转为数组，再打开，主要了解一下如何Image图片转为数组
import numpy as np
imgarray = np.array(Image.open('01.jpg'))
img = Image.fromarray(imgarray)