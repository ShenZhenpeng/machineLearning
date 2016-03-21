# -*- coding: UTF-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
"""
k-近邻算法
classify0有4个输入参数：
    inX：用于分类的输入向量
    dataSet：训练样本集
    labels：标签向量
    k：选择最近邻居的数目
"""
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  #numpy.core.fromnumeric.shape读取矩阵的长度, shape[0]读取矩阵第一维度的长度
    """
    numpy.lib.shape_base.tile用来重复某个数组
    a = [0, 1, 2]
    tile(a, 2)
    >>>array([0,1,2,0,1,2])
    tile(a, (1,2))
    >>>array([0,1,2,0,1,2])
    tile(a, (2,1))
    >>>array([0,1,2],
        [0,1,2])
    """
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print diffMat
    sqDiffMat = diffMat**2
    print sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1)
    print sqDistances
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    print sortedDistIndicies
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group, labels = createDataSet()
print group
print labels

print "input"
print [1.1, 1.2]
print classify0([1.1, 1.2], group, labels, 3)
