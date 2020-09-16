#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gc_script.py
# @Time      :2020/9/15 3:19 下午
# @Author    :Kangke


import gc

'''
ref: https://foofish.net/python-gc.html
解决python当中的循环引用等问题
'''

# 垃圾回收
# 返回处理这些循环引用一共释放掉的对象个数
gc.collect()