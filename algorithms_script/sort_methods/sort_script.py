#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sort_script.py
# @Time      :2020/9/22 5:15 下午
# @Author    :Kangke


"""
字典排序，方法一
"""
d = {'a': 1, 'c': 3, 'b': 2}  # 首先建一个字典d
d_order = sorted(d.items(), key=lambda x: x[1], reverse=False)  # 按字典集合中，每一个元组的第二个元素排列。
print(d_order)  # 得到:  [('a', 1), ('b', 2), ('c', 3)]

"""
字典排序：方法二
"""
d = {'a': 1, 'c': 3, 'b': 2}  # 首先建一个字典d
d.items()  # 得到: dict_items([('a', 1), ('c', 3), ('b', 2)])
L = list(d.items())  # 得到列表: L=[('a', 1), ('c', 3), ('b', 2)]
L.sort(key=lambda x: x[1], reverse=False)  # 按列表中，每一个元组的第二个元素从小到大排序。
print(L)  # 得到:  [('a', 1), ('b', 2), ('c', 3)]

"""
字符串排序
"""
sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']


"""
元组排序
"""
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

"""
对类进行排序
"""


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

"""
使用operator函数进行排序
"""
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
sorted(student_objects, key=attrgetter('age'))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

"""
使用operator进行多级排序
"""
sorted(student_tuples, key=itemgetter(1,2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
sorted(student_objects, key=attrgetter('grade', 'age'))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]