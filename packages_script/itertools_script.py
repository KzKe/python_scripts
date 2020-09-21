#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :itertools_script.py
# @Time      :2020/9/20 10:47 下午
# @Author    :Kangke


"""
Ref: https://www.cnblogs.com/cython/articles/2169009.html
"""

"""
method 1: 
给出一组迭代器(iter1, iter2, ..., iterN)，
此函数创建一个新迭代器来将所有的迭代器链接起来，
返回的迭代器从iter1开始生成项，知道iter1被用完，
然后从iter2生成项，这一过程会持续到iterN中所有的项都被用完。
"""

from itertools import chain

test = chain('AB', 'CDE', 'F')
# for t in test:
#     print(t)


"""
method 2: 
一个备用链构造函数，其中的iterables是一个迭代变量，
生成迭代序列，此操作的结果与以下生成器代码片段生成的结果相同：
"""
from itertools import chain
test = chain.from_iterable('ABCDEF')

print(test.__next__())
print(test.__next__())

"""
method 3: 
创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序:
"""
from itertools import combinations

test = combinations([1,2,3,4], 2)
for el in test:
    print(el)

