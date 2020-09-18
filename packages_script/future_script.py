#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :future_script.py
# @Time      :2020/9/18 2:47 下午
# @Author    :Kangke

'''
先寻找系统路径的包导入
'''
from __future__ import  absolute_import

'''
兼容python2 和 python3的print函数
'''
from __future__ import print_function

'''
将模块中显式出现的所有字符串转为unicode类型，防止出现len计算不一致的情况
'''
from __future__ import  unicode_literals