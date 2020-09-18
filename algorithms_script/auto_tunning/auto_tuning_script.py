#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :auto_tuning_script.py
# @Time      :2020/9/18 3:37 下午
# @Author    :Kangke


from skopt import BayesSearchCV
from bayes_opt import BayesianOptimization
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.feature_selection import RFECV

