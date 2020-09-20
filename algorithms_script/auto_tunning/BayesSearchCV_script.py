#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :BayesSearchCV_script.py
# @Time      :2020/9/20 11:46 上午
# @Author    :Kangke

'''
https://scikit-optimize.github.io/stable/modules/generated/skopt.BayesSearchCV.html
'''

from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X,y = load_iris(True)
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    train_size=0.75,
                                                    random_state=0)

opt = BayesSearchCV(
    SVC(),
    {
        'C': Real(1e-6, 1e+6, prior='log-uniform'),
        'gamma': Real(1e-6, 1e+1, prior='log-uniform'),
        'degree': Integer(1,8),
        'kernel': Categorical(['linear', 'poly', 'rbf']),
    },
    n_iter=32,
    random_state=0
)

_ = opt.fit(X_train, y_train)
print(opt.score(X_test, y_test))

