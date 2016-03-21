# -*- coding: utf-8 -*-

from math import log
import operator

class decisionTree():
    def __init__(self):
        print 'decisionTree Build'

    """
    计算给定数据集的香农熵
    dataSet: 待计算的数据集
    """
    def calcShannonEnt(self, dataSet):
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
    def splittingInfo(self, dataSet):
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
    def splitDataSet(self, dataSet, axis, value):
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
    def chooseBestFeatureToSplit(self, dataSet):
        numFeatures = len(dataSet[0]) - 1
        baseEntropy = self.calcShannonEnt(dataSet)
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
                subDataSet = self.splitDataSet(dataSet, i, value)
                # print 'subDataSet'
                # print subDataSet
                prob = len(subDataSet)/float(len(dataSet))
                newEntropy += prob * self.calcShannonEnt(subDataSet)
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

    import operator

    """
    获取出现次数最多的分类名称
    """
    def majorityCnt(self, classList):
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
    def createTree(self, dataSet, labels):

        classList = [example[-1] for example in dataSet]
        if classList.count(classList[0]) == len(classList):
            return classList[0] # 类别完全相同则停止继续划分
        if len(dataSet[0]) == 1:
            return self.majorityCnt(classList) # 遍历玩所有特征时返回出现次数最多的
        bestFeat = self.chooseBestFeatureToSplit(dataSet)
        print 'bestFeat:'
        print bestFeat
        bestFeatLabel = labels[bestFeat]
        myTree = {bestFeatLabel: {}}
        del(labels[bestFeat])
        featValues = [example[bestFeat] for example in dataSet]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]
            myTree[bestFeatLabel][value] = self.createTree(self.splitDataSet(dataSet, bestFeat, value), subLabels)
        return myTree
