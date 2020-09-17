#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :argparse_script.py
# @Time      :2020/9/15 2:56 下午
# @Author    :Kangke

'''
中文文档：
https://docs.python.org/zh-cn/3/library/argparse.html
'''

import argparse

# (1) 声明一个parser
parser = argparse.ArgumentParser()
# (2) 添加参数
parser.add_argument("parg")  # 位置参数，这里表示第一个出现的参数赋值给parg
parser.add_argument("--digit", type=int, help="输入数字")  # 通过 --echo xxx声明的参数，为int类型
parser.add_argument("--name", help="名字", default="cjf")  # 同上，default 表示默认值
parser.add_argument("--shownames", type=str, help='show parameters', default='none')
# (3) 读取命令行参数
args = parser.parse_args()

# 自己添加参数
args.text = 'nihao'
args.secondparameter = '22222'

# (4) 调用这些参数
print(args.parg)
print("echo ={0}".format(args.digit))
print("name = {0}".format(args.name))
print('paramters = {0}'.format(args.text))
print('second parameter = {}'.format((args.secondparameter)))

print('-'*20)
parser.print_help()