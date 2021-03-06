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
from sklearn.tree import DecisionTreeClassifier
from math import log
import operator


# 训练数据
# load the CSV file as a numpy matrix
f = open("training.csv")
f.readline()
training_data = np.loadtxt(f, delimiter=",")
X = training_data[:, 0:5]
y = training_data[:, 5]
dataSetNumpy = training_data[:, 0:6]
dataSet = dataSetNumpy.tolist()
# print dataSet
# print X.shape, y.shape

# a1 = np.array([[1, 2, 3], [2, 3, 4]], dtype=int)
#
# b1 = np.zeros((2, 3))
#
#
# for item in X:
#     print item





# 测试数据
f2 = open("testing.csv")
f2.readline()
testing_data = np.loadtxt(f2, delimiter=",")
X_test = testing_data[:261, 0:5]
y_test = testing_data[:261, 5]
dataSetTest = dataSetNumpy.tolist()

#
#
# # fit a SVM model to the data
# model = DecisionTreeClassifier()
# model.fit(X, y)
# print(model)
#
# # make predictions
# expected = y_test
# predicted = model.predict(X_test)
# # summarize the fit of the model
# print expected
# print predicted
#
# safe_cnt = 0
# shell_cnt = 0
# for p in predicted:
#     if p == 0.0:
#         safe_cnt += 1
#     else:
#         shell_cnt += 1
# print "not webshell count:", safe_cnt
# print "webshell count:", shell_cnt
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))









"""
[学号，性别（女：0，男：1），是否学生干部（否：0， 是：1），综合成绩（0-59:0，60-69：1，70-79: 2， 80-89:3， 90-100：4），毕业论文(不及格：0，及格：1，中：2，良：3，优：4)，就业情况（未就业：0，已就业：1）]
"""
# 数据创建函数
def createDataSet():
    # 数据含义

    dataSet = [[2000041134, 1, 1, 2, 4, 1],
           [2000041135, 0, 1, 3, 2, 1],
           [2000041201, 1, 0, 1, 0, 0],
           [2000041202, 1, 1, 1, 3, 1],
           [2000041203, 1, 1, 2, 2, 1],
           [2000041204, 1, 0, 2, 3, 0],
           [2000041205, 0, 1, 1, 3, 1],
           [2000041209, 1, 1, 1, 3, 1],
           [2000041210, 0, 1, 2, 2, 0],
           [2000041211, 1, 0, 1, 1, 1],
           [2000041215, 1, 1, 3, 1, 1],
           [2000041216, 1, 1, 2, 3, 1],
           [2000041223, 1, 0, 2, 1, 0],
           [2000041319, 1, 0, 1, 1, 1],
           [2000041320, 1, 1, 2, 3, 1],
           [2000041321, 1, 0, 2, 3, 0],
           [2000041322, 1, 0, 3, 3, 0],
           [2000041323, 0, 1, 2, 3, 1],
           [2000041324, 1, 0, 2, 0, 0],
           [2000041325, 1, 0, 2, 3, 0],
           [2000041326, 0, 1, 1, 4, 1],
           [2000041327, 1, 1, 1, 3, 1]]
    dataSet1 = [[1, 1, 2, 4, 1],
           [0, 1, 3, 2, 1],
           [1, 0, 1, 0, 0],
           [1, 1, 1, 3, 1],
           [1, 1, 2, 2, 1],
           [1, 0, 2, 3, 0],
           [0, 1, 1, 3, 1],
           [1, 1, 1, 3, 1],
           [0, 1, 2, 2, 0],
           [1, 0, 1, 1, 1],
           [1, 1, 3, 1, 1],
           [1, 1, 2, 3, 1],
           [1, 0, 2, 1, 0],
           [1, 0, 1, 1, 1],
           [1, 1, 2, 3, 1],
           [1, 0, 2, 3, 0],
           [1, 0, 3, 3, 0],
           [0, 1, 2, 3, 1],
           [1, 0, 2, 0, 0],
           [1, 0, 2, 3, 0],
           [0, 1, 1, 4, 1],
           [1, 1, 1, 3, 1]]
    labels = ['学号', '性别', '是否学生干部','综合成绩','毕业论文']
    labels1 = ['性别', '是否学生干部','综合成绩','毕业论文']
    labels2 = ['A', 'B', 'C', 'D', 'E']
    return dataSet, labels2

"""
计算给定数据集的香农熵
dataSet: 待计算的数据集
"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt = shannonEnt - prob*log(prob, 2) # 以2为底求对数
    return shannonEnt

"""
分裂信息(信息增益比例)
"""
def splittingInfo(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt = shannonEnt - prob*log(prob, 2) # 以2为底求对数
    return shannonEnt


"""
按照指定特征划分数据集
params:
dataSet:待划分的数据集
axis:划分数据集的特征
value:特征的返回值
"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

"""
选择最好的数据集划分方式
函数使用要求：
    1.数据必须是一种列表元素组成的列表
    2.数据的最后一列或者每个实例的最后一个元素是当前实例的类别标签
"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestgainRatio = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        feature = [example[i] for example in dataSet]
        # 创建唯一的标签分类列表
        # print "feature:"
        # print feature
        uniqueVals = set(feature)
        # print "uniqueVals::"
        # print uniqueVals
        newEntropy = 0.0
        splitInfo = 0.0
        for value in uniqueVals:
			# 把第i个数据去掉，然后计算现在的香农熵
            subDataSet = splitDataSet(dataSet, i, value)
            # print 'subDataSet'
            # print subDataSet
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            splitInfo -= prob*log(prob, 2)
            # print "prob::"
            # print prob
            # print "splitInfo::"
            # print splitInfo
        infoGain = baseEntropy - newEntropy
        gainRatio = infoGain/(splitInfo+1)
        # print "gainRatio:"
        # print gainRatio
        # 计算最好的信息增益率
        if (gainRatio > bestgainRatio):
            bestgainRatio = gainRatio
            bestFeature = i
    return bestFeature

# myDat, labels = createDataSet()
# print chooseBestFeatureToSplit(myDat)
# print myDat


"""
获取出现次数最多的分类名称
"""
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sotedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)# 使用operator操作键值排序字典
    return sotedClassCount[0][0]

"""
创建树的函数代码
"""
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0] # 类别完全相同则停止继续划分
    if len(dataSet[0]) == 1:
        return majorityCnt(classList) # 遍历玩所有特征时返回出现次数最多的
    bestFeat = chooseBestFeatureToSplit(dataSet)
    print 'bestFeat:'
    print bestFeat
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


# myDat, labels = createDataSet()
# myTree = createTree(myDat, labels)
#

labels = ['LanguageIC', 'Entropy', 'LongestWord', 'SignatureNasty', 'SignatureSuperNasty']
# print dataSet
# print labels
def getHandlerData(dataSet):
    for i in range(dataSet.__len__()):
        dataSet[i][0] = int(dataSet[i][0] * 100)
        dataSet[i][1] = int(dataSet[i][1] * 10)
        dataSet[i][2] = int(dataSet[i][2]/10)
        if(dataSet[i][2] > 20):
            dataSet[i][2] = 20
        dataSet[i][3] = int(dataSet[i][3]/5)
        if(dataSet[i][3] > 10):
            dataSet[i][3] = 10
        dataSet[i][4] = int(dataSet[i][4]/5)
        if(dataSet[i][4] > 10):
            dataSet[i][4] = 10
    return dataSet

dataSet = getHandlerData(dataSet)
dataSetTest = getHandlerData(dataSetTest)

print 'dataSet::'
print dataSet
print '============================================================================='
print 'dataSetTest::'
print dataSetTest

myTree = createTree(dataSet, labels)
print myTree

safe_cnt = 0
shell_cnt = 0
for p in dataSetTest:
    if p[5] == 0.0:
        safe_cnt += 1
    else:
        shell_cnt += 1
print "not webshell count:", safe_cnt
print "webshell count:", shell_cnt


labels = ['LanguageIC', 'Entropy', 'LongestWord', 'SignatureNasty', 'SignatureSuperNasty']
def checkFunc(checkdata, tree):
    for i in range(labels.__len__()):
        label = labels[i]
        if type(tree) ==float or type(tree) == int:
            return tree
        if tree.has_key(label):
            # print label
            # print tree
            childTree = tree[label]
            data = checkdata[i]
            # print data
            childTree = childTree[data]
            # print childTree
            if isinstance(childTree, int):
                return childTree
            return checkFunc(checkdata, childTree)

# print myTree
checkList = []
resultList = []
for data in dataSetTest:
    checkList.append(checkFunc(data, myTree))
    resultList.append(data[5])
    # print checkList
print checkList
print resultList


print '总数:', resultList.__len__()
print '总数:', checkList.__len__()
wubaoNum = 0
noNum = 0

for i in range(resultList.__len__()):
    if resultList[i]==0.0 and checkList[i]==1.0:
        wubaoNum=wubaoNum+1
    if resultList[i]==1.0 and checkList[i]==0.0:
        noNum=noNum+1

print '误报数：', wubaoNum
print '遗漏数：', noNum

print '误报率：', float(wubaoNum)/resultList.__len__()
print '遗漏数：', float(noNum)/resultList.__len__()



# 下面对mytree数据进行预处理，调整好阶梯

# print myTree