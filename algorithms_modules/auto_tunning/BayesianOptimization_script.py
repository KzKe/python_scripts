#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BayesianOptimization_script.py
# @Time      :2020/9/20 12:05 下午
# @Author    :Kangke

'''
https://www.jianshu.com/p/92d8943fb0ba
'''

from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

x, y = make_classification(n_samples=1000, n_features=10, n_classes=2)

gbdt = GradientBoostingClassifier()
cross_val_score(gbdt, x, y, cv=20, scoring='roc_auc').mean()
### 结果是：0.952

from bayes_opt import BayesianOptimization


def gbdt_cv(n_estimators, min_samples_split, max_features, max_depth):
    res = cross_val_score(
        GradientBoostingClassifier(n_estimators=int(n_estimators),
                                   min_samples_split=int(min_samples_split),
                                   max_features=min(max_features, 0.999),  # float
                                   max_depth=int(max_depth),
                                   random_state=2
                                   ),
        x, y, scoring='roc_auc', cv=20
    ).mean()
    return res


gbdt_op = BayesianOptimization(
    gbdt_cv,
    {'n_estimators': (10, 250),
     'min_samples_split': (2, 25),
     'max_features': (0.1, 0.999),
     'max_depth': (5, 15)}
)

gbdt_op.maximize()

print(gbdt_op.max)
