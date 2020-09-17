#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :copy_script.py
# @Time      :2020/9/15 3:06 下午
# @Author    :Kangke

'''
Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。
1、copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
2、copy.deepcopy 深拷贝 拷贝对象及其子对象

copy只拷贝到第一级，对更深的数据还是采用引用拷贝
deepcopy对深层的数据也会进行拷贝
但是如果完全改变了原始数据的地址，拷贝后的数据不会有任何改变
'''
import copy
a = [1,2,3,4,['a','b']]  #原始对象>>> b = a  #赋值，传对象的引用
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')

print('a=', a)
# a= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('b=', b)
# b= [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print('c=', c)
# c= [1, 2, 3, 4, ['a', 'b', 'c']]
print('d=', d)
# d= [1, 2, 3, 4, ['a', 'b']]
