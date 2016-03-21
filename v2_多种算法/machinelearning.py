# -*- coding: utf-8 -*-
import numpy as np
from sklearn import preprocessing
training = "training0225.csv"
training_data = np.loadtxt(open(training,"r"), delimiter=",")
X = training_data[:,0:4]
y = training_data[:,5]
# 归一化
# normalized_X = preprocessing.normalize(X)
# print normalized_X
# print preprocessing.scale(X)

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
# 参数调优
from scipy.stats import uniform as sp_rand
from sklearn.linear_model import Ridge
from sklearn.grid_search import RandomizedSearchCV
for x in range(0,6):
	if x == 0:
		# 逻辑回归
		algorithm_mode = "逻辑回归"
		model = LogisticRegression()
	elif x == 1:
		# 朴素贝叶斯
		algorithm_mode = "朴素贝叶斯"
		model = GaussianNB()
	elif x == 2:
		# 支持向量机
		algorithm_mode = "支持向量机"
		model = SVC()
	elif x == 3:
		# 树算法
		algorithm_mode = "树算法"
		model = ExtraTreesClassifier()
	elif x == 4:
		# k近邻
		algorithm_mode = "k近邻"
		model = KNeighborsClassifier()
	elif x == 5:
		# 决策树
		algorithm_mode = "决策树"
		model = DecisionTreeClassifier()

	"""
	# 参数调优
	# prepare a uniform distribution to sample for the alpha parameter
	param_grid = {'alpha': sp_rand()}
	# create and fit a ridge regression model, testing random alpha values
	model = Ridge()
	rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)
	rsearch.fit(X, y)
	print(rsearch)
	# summarize the results of the random parameter search
	print(rsearch.best_score_)
	print(rsearch.best_estimator_.alpha)
	"""
	# model.fit(normalized_X,y)
	model.fit(X,y)
	# print(model)
	testing = "testing0225.csv"
	testing_data = np.loadtxt(open(testing,"r"), delimiter=",")
	X_t = testing_data[:,0:4]
	y_t = testing_data[:,5]
	expected=y_t
	# normalized_X_t = preprocessing.normalize(X_t)
	# predicted=model.predict(normalized_X_t)

	predicted=model.predict(X_t)
	shell_count = 0
	normal_count = 0
	for predict in predicted:
		if predict==0.0:
			normal_count += 1
		else:
			shell_count += 1
		# normal_count+=1 if x==0.0 else shell_count+=1


	results = metrics.classification_report(expected, predicted)
	counts = metrics.confusion_matrix(expected, predicted)
	# print(predicted)
	# print(results)
	# print(counts)
	real_normal_count = int(results.split("\n")[2].split(" ")[-1:][0])
	real_shell_count = int(results.split("\n")[3].split(" ")[-1:][0])
	print "="*50
	print "使用的算法: ", algorithm_mode
	print
	print "详情: "
	print "\t正常文件中: "
	print "\t判定为正常文件: ", counts[0][0], ", 判定为webshell: ", counts[0][1]
	print "\twebshell中: "
	print "\t判定为正常文件: ", counts[1][0], ", 判定为webshell: ", counts[1][1]
	print "总体分数: "
	print results
	print "总结: "
	print "判定为shell: ", shell_count, ", 实际应为: ", real_shell_count
	print "判断为正常: ", normal_count, ", 实际应为: ", real_normal_count
	print "误报率: ", "%.2f%%" % (100*float(counts[0][1])/real_normal_count), "(将正常文件判断为webshell/实际正常文件数)"
	print "漏报率: ", "%.2f%%" % (100*float(counts[1][0])/real_shell_count), "(将webshell判断为正常文件/实际webshell数)"



"""
==================================================
使用的算法:  逻辑回归

详情:
	正常文件中:
	判定为正常文件:  3199 , 判定为webshell:  18
	webshell中:
	判定为正常文件:  50 , 判定为webshell:  80
总体分数:
             precision    recall  f1-score   support

        0.0       0.98      0.99      0.99      3217
        1.0       0.82      0.62      0.70       130

avg / total       0.98      0.98      0.98      3347

总结:
判定为shell:  98 , 实际应为:  130
判断为正常:  3249 , 实际应为:  3217
误报率:  0.56% (将正常文件判断为webshell/实际正常文件数)
漏报率:  38.46% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  朴素贝叶斯

详情:
	正常文件中:
	判定为正常文件:  3201 , 判定为webshell:  16
	webshell中:
	判定为正常文件:  63 , 判定为webshell:  67
总体分数:
             precision    recall  f1-score   support

        0.0       0.98      1.00      0.99      3217
        1.0       0.81      0.52      0.63       130

avg / total       0.97      0.98      0.97      3347

总结:
判定为shell:  83 , 实际应为:  130
判断为正常:  3264 , 实际应为:  3217
误报率:  0.50% (将正常文件判断为webshell/实际正常文件数)
漏报率:  48.46% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  支持向量机

详情:
	正常文件中:
	判定为正常文件:  3046 , 判定为webshell:  171
	webshell中:
	判定为正常文件:  24 , 判定为webshell:  106
总体分数:
             precision    recall  f1-score   support

        0.0       0.99      0.95      0.97      3217
        1.0       0.38      0.82      0.52       130

avg / total       0.97      0.94      0.95      3347

总结:
判定为shell:  277 , 实际应为:  130
判断为正常:  3070 , 实际应为:  3217
误报率:  5.32% (将正常文件判断为webshell/实际正常文件数)
漏报率:  18.46% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  树算法

详情:
	正常文件中:
	判定为正常文件:  3122 , 判定为webshell:  95
	webshell中:
	判定为正常文件:  13 , 判定为webshell:  117
总体分数:
             precision    recall  f1-score   support

        0.0       1.00      0.97      0.98      3217
        1.0       0.55      0.90      0.68       130

avg / total       0.98      0.97      0.97      3347

总结:
判定为shell:  212 , 实际应为:  130
判断为正常:  3135 , 实际应为:  3217
误报率:  2.95% (将正常文件判断为webshell/实际正常文件数)
漏报率:  10.00% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  k近邻

详情:
	正常文件中:
	判定为正常文件:  3134 , 判定为webshell:  83
	webshell中:
	判定为正常文件:  35 , 判定为webshell:  95
总体分数:
             precision    recall  f1-score   support

        0.0       0.99      0.97      0.98      3217
        1.0       0.53      0.73      0.62       130

avg / total       0.97      0.96      0.97      3347

总结:
判定为shell:  178 , 实际应为:  130
判断为正常:  3169 , 实际应为:  3217
误报率:  2.58% (将正常文件判断为webshell/实际正常文件数)
漏报率:  26.92% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  决策树

详情:
	正常文件中:
	判定为正常文件:  2877 , 判定为webshell:  340
	webshell中:
	判定为正常文件:  12 , 判定为webshell:  118
总体分数:
             precision    recall  f1-score   support

        0.0       1.00      0.89      0.94      3217
        1.0       0.26      0.91      0.40       130

avg / total       0.97      0.89      0.92      3347

总结:
判定为shell:  458 , 实际应为:  130
判断为正常:  2889 , 实际应为:  3217
误报率:  10.57% (将正常文件判断为webshell/实际正常文件数)
漏报率:  9.23% (将webshell判断为正常文件/实际webshell数)
"""











































"""
==================================================
使用的算法:  逻辑回归

详情:
	正常文件中:
	判定为正常文件:  3192 , 判定为webshell:  18
	webshell中:
	判定为正常文件:  33 , 判定为webshell:  39
总体分数:
             precision    recall  f1-score   support

        0.0       0.99      0.99      0.99      3210
        1.0       0.68      0.54      0.60        72

avg / total       0.98      0.98      0.98      3282

总结:
判定为shell:  57 , 实际应为:  72
判断为正常:  3225 , 实际应为:  3210
误报率:  0.56% (将正常文件判断为webshell/实际正常文件数)
漏报率:  45.83% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  朴素贝叶斯

详情:
	正常文件中:
	判定为正常文件:  3198 , 判定为webshell:  12
	webshell中:
	判定为正常文件:  44 , 判定为webshell:  28
总体分数:
             precision    recall  f1-score   support

        0.0       0.99      1.00      0.99      3210
        1.0       0.70      0.39      0.50        72

avg / total       0.98      0.98      0.98      3282

总结:
判定为shell:  40 , 实际应为:  72
判断为正常:  3242 , 实际应为:  3210
误报率:  0.37% (将正常文件判断为webshell/实际正常文件数)
漏报率:  61.11% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  支持向量机

详情:
	正常文件中:
	判定为正常文件:  3069 , 判定为webshell:  141
	webshell中:
	判定为正常文件:  11 , 判定为webshell:  61
总体分数:
             precision    recall  f1-score   support

        0.0       1.00      0.96      0.98      3210
        1.0       0.30      0.85      0.45        72

avg / total       0.98      0.95      0.96      3282

总结:
判定为shell:  202 , 实际应为:  72
判断为正常:  3080 , 实际应为:  3210
误报率:  4.39% (将正常文件判断为webshell/实际正常文件数)
漏报率:  15.28% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  树算法

详情:
	正常文件中:
	判定为正常文件:  2755 , 判定为webshell:  455
	webshell中:
	判定为正常文件:  4 , 判定为webshell:  68
总体分数:
             precision    recall  f1-score   support

        0.0       1.00      0.86      0.92      3210
        1.0       0.13      0.94      0.23        72

avg / total       0.98      0.86      0.91      3282

总结:
判定为shell:  523 , 实际应为:  72
判断为正常:  2759 , 实际应为:  3210
误报率:  14.17% (将正常文件判断为webshell/实际正常文件数)
漏报率:  5.56% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  k近邻

详情:
	正常文件中:
	判定为正常文件:  3130 , 判定为webshell:  80
	webshell中:
	判定为正常文件:  24 , 判定为webshell:  48
总体分数:
             precision    recall  f1-score   support

        0.0       0.99      0.98      0.98      3210
        1.0       0.38      0.67      0.48        72

avg / total       0.98      0.97      0.97      3282

总结:
判定为shell:  128 , 实际应为:  72
判断为正常:  3154 , 实际应为:  3210
误报率:  2.49% (将正常文件判断为webshell/实际正常文件数)
漏报率:  33.33% (将webshell判断为正常文件/实际webshell数)
==================================================
使用的算法:  决策树

详情:
	正常文件中:
	判定为正常文件:  2578 , 判定为webshell:  632
	webshell中:
	判定为正常文件:  3 , 判定为webshell:  69
总体分数:
             precision    recall  f1-score   support

        0.0       1.00      0.80      0.89      3210
        1.0       0.10      0.96      0.18        72

avg / total       0.98      0.81      0.87      3282

总结:
判定为shell:  701 , 实际应为:  72
判断为正常:  2581 , 实际应为:  3210
误报率:  19.69% (将正常文件判断为webshell/实际正常文件数)
漏报率:  4.17% (将webshell判断为正常文件/实际webshell数)
"""
