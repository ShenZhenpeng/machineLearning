# -*- coding: utf-8 -*-

__author__ = 'shenzp'

# yield Test

def gen():
    print 'enter'
    yield 1
    print 'next'
    yield 3
    print 'next again'

for i in gen():
    print i


array = [i for i in range(10)]

for i in array:
    print i


# def inorder(t):
#     if t:
#         for x in inorder(t.left):
#             yield x
#         yield t.label
#         for x in inorder(t.right):
#             yield x
#
# for n in inorder(tree):
#     print n


def fun():
    print 'start...'
    m = yield 5
    print m
    print 'middle...'
    d = yield 12
    print d
    print 'end...'

# send函数实质上与next()是相似的，区别是send是传递yield表达式的值进去，
# 而next不能传递特定的值，只能传递None进去，因此可以认为g.next()和g.send(None)是相同的

m = fun()
m.next()
m.send('message')
m.next()