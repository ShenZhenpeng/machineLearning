#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import numpy as np
from sklearn import metrics
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import cross_validation
from sklearn.metrics import classification_report

# 训练数据
# load the CSV file as a numpy matrix
f = open("training.csv")
f.readline()
training_data = np.loadtxt(f, delimiter=",")
X = training_data[:, 0:5]
y = training_data[:, 5]
#print X.shape, y.shape

# 测试数据
f2 = open("testing.csv")
f2.readline()
testing_data = np.loadtxt(f2, delimiter=",")
X_test = testing_data[:261, 0:5]
y_test = testing_data[:261, 5]
#print X_test.shape, y_test.shape

#(data, target) = (iris.data, iris.target)
(data, target) = (X,y)
#print(data,target)
clf = GaussianNB()
# (data, target) = (digits.data, digits.target)
# clf = MultinomialNB()
X_tr, X_tt, y_tr, y_tt = cross_validation.train_test_split(data, target, test_size = 0.5, random_state = 0)

clf.fit(X_tr, y_tr)
y_true, y_pred = y_tt, clf.predict(X_tt)
count = 0
for left , right in zip(y_true,y_pred):
    if left == right:
        count += 1
print(count,len(y_true),float(count)/len(y_true))

print(metrics.classification_report(y_true, y_pred))
print(metrics.confusion_matrix(y_true, y_pred))
