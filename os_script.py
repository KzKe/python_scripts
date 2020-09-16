#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :os_script.py
# @Time      :2020/9/16 11:29 上午
# @Author    :Kangke


import os
import sys

# generate config
curPath = os.path.abspath(os.path.dirname(__file__))
# 获取项目的根目录
root_path = os.path.split(os.path.split(curPath)[0])[0]
sys.path.append(os.path.split(root_path)[0])
########################################

path = os.getcwd()
# 创建文件夹
os.makedirs('dir1/dir2')  # 可生成多层递归目录
os.mkdir('dir3')  # 生成单级目录；相当于shell中mkdir dirname
os.mkdir('dir3/dir4')

# 只能删空文件夹
os.rmdir('dir3/dir4') # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.removedirs('dir3/dir4') # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.removedirs('dir1/dir2')

os.listdir('dirname')   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove() # 删除一个文件
os.rename("oldname", "newname")  # 重命名文件/目录
os.stat('path/filename') # 获取文件/目录信息

os.path.abspath(path)  # 返回path规范化的绝对路径
os.path.split(path)  # 将path分割成目录和文件名二元组返回
os.path.dirname(path)  # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

os.system("bash command")  # 运行shell命令，直接显示
os.popen("bash command").read()  # 运行shell命令，获取执行结果
os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd

os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  # 如果path是绝对路径，返回True
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False

path1 = os.getcwd()
os.path.join(path1, path)  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  # 返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path)  # 返回path的大小
