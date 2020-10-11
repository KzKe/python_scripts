#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: KeKang
@contact:***@**.com
@version: 1.0.0
@license: Apache Licence
@file: jieba_script.py
@time: 2020/10/10 5:54 下午
"""
import jieba

"""
添加和删除jieba分词的词库。
"""
for word in ['花呗', '借呗', '支付宝', '余额宝', '饿了么', '微粒贷', '双十一',
             '小蓝车', '拼多多', '外卖', '美团', '账单', '到账', '能不能', '应还', '会不会',
             '找不到', '另一个', '微信', '网商贷']:
    jieba.add_word(word)
for word in ["开花", "开了花", "提花", "申花", "天花", "银花", "我花", "借花"]:
    jieba.del_word(word)


word_list = jieba.cut('我开始使用花呗了,拼多多支付宝饿了饿了么')
print(list(word_list))
