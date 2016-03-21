#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: cy陈莹(IT) <ying.chen@Ctrip.com>
# Created on 2016/2/18
#
# webshell检测
# 
# 样本：Tdifg/webshell: https://github.com/tdifg/WebShell.git
#       Tanjiti:https://github.com/tanjiti/webshellSample.git
#       PHPCMS
# 特征: NeoPI的五个特征
# 算法：SVM
# 

import numpy as np
from sklearn import metrics
from sklearn.svm import SVC
from math import log

# 训练数据
# load the CSV file as a numpy matrix
f = open("training.csv")
f.readline()
training_data = np.loadtxt(f, delimiter=",")
X = training_data[:, 0:5]
y = training_data[:, 5]
print X.shape, y.shape

# 测试数据
f2 = open("testing.csv")
f2.readline()
testing_data = np.loadtxt(f2, delimiter=",")
X_test = testing_data[:261, 0:5]
y_test = testing_data[:261, 5]
print X_test.shape, y_test.shape


# fit a SVM model to the data
model = SVC()
model.fit(X, y)
print(model)

# make predictions
expected = y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print predicted

safe_cnt = 0
shell_cnt = 0
for p in predicted:
    if p == 0.0:
        safe_cnt += 1
    else:
        shell_cnt += 1
print "not webshell count:", safe_cnt
print "webshell count:", shell_cnt
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))