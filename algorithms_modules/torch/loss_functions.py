#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: KeKang
@contact:***@**.com
@version: 1.0.0
@license: Apache Licence
@file: loss_functions.py
@time: 2020/10/10 7:18 下午
"""
import torch


def dice_loss(pred, target):
    """ dice loss for unbalanced data training (deprecated) """
    smooth = 1.

    iflat = pred.view(-1)
    tflat = target.view(-1)
    intersection = (iflat * tflat).sum()

    return 1 - ((2. * intersection + smooth) /
                (iflat.sum() + tflat.sum() + smooth))


if __name__ == '__main__':
    x = 1
