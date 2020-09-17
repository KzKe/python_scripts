#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :tqdm_script.py
# @Time      :2020/9/15 3:23 下午
# @Author    :Kangke

'''
基础应用
'''
from tqdm import tqdm, trange
import time

for i in trange(100):
    time.sleep(0.1)
    pass

##################

from tqdm import tqdm
import time

pbar = tqdm(["a", "b", "c", "d"])
for c in pbar:
    time.sleep(1)
    pbar.set_description("Processing %s" % c)

'''
在pandas中使用tqdm
'''
import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
tqdm.pandas(desc="my bar!")
df.progress_apply(lambda x: x ** 2)

'''
进度条，后面显示信息
'''
from tqdm import trange
from random import random, randint
import time

with trange(100) as t:
    for i in t:
        # 设置进度条左边显示的信息
        t.set_description("GEN %i" % i)
        # 设置进度条右边显示的信息
        t.set_postfix(loss=random(), gen=randint(1, 999), str="h", lst=[1, 2])
        time.sleep(0.1)

'''

'''
from tqdm import tqdm
import time

# total参数设置进度条的总长度
with tqdm(total=100) as pbar:
    for i in range(100):
        time.sleep(0.05)
        # 每次更新进度条的长度
        pbar.update(1)