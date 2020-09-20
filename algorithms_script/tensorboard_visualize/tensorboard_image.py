#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tensorboard_image.py
# @Time      :2020/9/21 7:39 上午
# @Author    :Kangke


from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

image = Image.open('elephant.jpg')
image = np.array(image)
# print(image.shape, image.dtype)

writer = SummaryWriter('tlogs')
writer.add_image('test', image, 1,dataformats='HWC')
writer.close()