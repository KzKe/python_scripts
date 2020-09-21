#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gensim_w2v_read.py
# @Time      :2020/9/21 10:46 上午
# @Author    :Kangke

from gensim import models

w2v = models.KeyedVectors.load_word2vec_format(
    root_path + '/model/embedding/w2v.bin', binary=False)

if __name__ == "__main__":
    run_code = 0