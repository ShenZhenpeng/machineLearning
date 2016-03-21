# -*- encoding:utf-8 -*-

from math import log

# 计算给定数据集的香农熵
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

# 数据创建函数
def createDataSet():
    # 数据含义（不浮出水面是否可以生存， 是否有脚蹼，属于鱼类）
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
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
    dataSet2 = [[2000041134, 1, 1, 2, 4, 1],
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
    labels = ['no surfacing', 'flippers']
    labels1 = ['A', 'B','C','D']
    return dataSet2, labels1

myDat, labels = createDataSet()
print myDat
print labels
print calcShannonEnt(myDat)

myDat[0][-1] = 'maybe'
print myDat
print calcShannonEnt(myDat)

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
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        feature = [example[i] for example in dataSet]
        # 创建唯一的标签分类列表
        print "feature:"
        print feature
        uniqueVals = set(feature)
        print "uniqueVals::"
        print uniqueVals
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            print 'subDataSet'
            print subDataSet
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        print "infoGain:"
        print infoGain
        # 计算最好的信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

# myDat, labels = createDataSet()
# print chooseBestFeatureToSplit(myDat)
# print myDat

import operator

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
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myDat, labels = createDataSet()
myTree = createTree(myDat, labels)

print myTree
