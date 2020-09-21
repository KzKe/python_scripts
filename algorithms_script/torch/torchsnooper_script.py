#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :torchsnooper_script.py
# @Time      :2020/9/18 8:56 上午
# @Author    :Kangke


'''
ref: https://www.jiqizhixin.com/articles/2019-06-17-12
doc: https://github.com/zasdfgbnm/TorchSnooper
torch 参数调试利器，可以打印参数的类型，形状，device等信息
'''

import torch
import torchsnooper

model = torch.nn.Linear(2, 1)

x = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = torch.tensor([3.0, 5.0, 4.0, 6.0])

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

with torchsnooper.snoop():
    for _ in range(10):
        optimizer.zero_grad()
        pred = model(x)
        squared_diff = (y - pred) ** 2
        loss = squared_diff.mean()
        print(loss.item())
        loss.backward()
        optimizer.step()