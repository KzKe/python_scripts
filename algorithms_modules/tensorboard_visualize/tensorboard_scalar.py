#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tensorboard_script.py
# @Time      :2020/9/21 7:24 上午
# @Author    :Kangke


from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('tlogs')

# 添加数字
for i in range(100):
    writer.add_scalar('y=x2', i*i, i)

writer.close()

'''
运行方法：tensorboard --logdir='algorithms_modules/tensorboard_visualize'  
'''
