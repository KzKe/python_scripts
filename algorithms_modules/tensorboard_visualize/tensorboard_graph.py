#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tensorboard_graph.py
# @Time      :2020/9/21 7:49 上午
# @Author    :Kangke

"""
添加模型到 tensorboardX
"""

import torch
import torchvision
from torch.autograd import Variable
from tensorboardX import SummaryWriter

input_data = Variable(torch.rand(16, 3, 224, 224))

net = torchvision.models.resnet18()

writer = SummaryWriter(log_dir='./tlogs', comment='resnet18')

with writer:
    writer.add_graph(net, (input_data, ))

