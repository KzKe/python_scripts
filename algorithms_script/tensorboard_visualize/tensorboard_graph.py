#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tensorboard_graph.py
# @Time      :2020/9/21 7:49 上午
# @Author    :Kangke


from torch.utils.tensorboard import SummaryWriter


writer = SummaryWriter('tlogs')

'''
添加网络结构
'''

writer.add_graph()