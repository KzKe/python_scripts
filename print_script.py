#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :print_script.py
# @Time      :2020/9/16 10:06 上午
# @Author    :Kangke


print('test01','test001','test0001',sep='*******') #输出多个对象需，分隔，注意这里相当于sep=''
# 输出：test01*******test001*******test0001


'''
格式化输出
# 在Python3 中print 是一个函数,通过格式化函数format()来控制输出格式

# 1. 通过位置标号
# {0}表示第一个元素， {1}表示第二个元素， {2}表示第三个元素，以此类推。。。
'''

a = 'Ace'
b = 'hello'
print("{1}, my name is {0}".format(a, b))
# hello, my name is Ace

'''
2. 通过关键词参数
'''
name = "Ace"
age = 26
print("{myname}'s age is {myage}".format(myname=name, myage=age))
# Ace's age is 26

'''
3. 通过属性和下标
'''
person = ["Ace", 26]
print("{0[0]}'s age is {0[1]}".format(person))
# Ace's age is 26

print("{people[0]}'s age is {people[1]}".format(people=person))
# Ace's age is 26

'''
字典字符串不需要加引号
'''
person = {'Ace': 26}
print("{myname}'s age is {people[Ace]}".format(myname=name,people=person))
# Ace's age is 26


'''
4. 格式化限定符
{0:0.3f} {1:3d} 在序号后面加上格式符就可以了，不用加%

5.填充与对齐
^,<,>分别代表居住，左对齐，右对齐，后面带宽度
'''
a = 123.456789
haha = 'haha!!!'
print("{0:0.3f}, *{1:<14}*".format(a, haha))
print("{0:0.3f}, *{1:>14}*".format(a, haha))
print("{0:0.3f}, *{1:^14}*".format(a, haha))
print("{0:0.3f}, *{1:}*".format(a, haha))

# 123.457, *haha!!!    *
# 123.457, *    haha!!!*
# 123.457, *  haha!!!  *
# 123.457, *haha!!!*











