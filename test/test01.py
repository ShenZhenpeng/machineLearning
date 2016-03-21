#!/usr/bin/python
# -*- encoding: utf-8 -*-

print 9//2
print 9.0//2.0


a = 10
b = 20
if a == b:
    print 'a == b'

if a != b:
    print 'a != b'

if a <> b:
    print 'a <> b'



a = 20
b = 20

if a is b:
    print 'a is b'
else:
    print 'a is not b'

a = { a: 'helllo' }
# b = { a: 'hello' }

print a
print 'a' in a
print 20 in a


for letter in 'python':
    if letter is 'h':
        pass
        print 'this is pass block'
    print 'Current Letter', letter


var1 = 3
print type(var1)

var2 = 3.3
var2 = 2.5e2
print type(var2)

var3 = 33l
print type(var3)

var4 = 1 + 2j
print type(var4)


print var1 + var2

x, y = 4, 3

print x, y
print cmp(y, x)
if cmp(y, x):
    print 'x>y'
else:
    print 'x<y'

import math
import random
x = -3
print type(abs(x))
print type(math.fabs(x))

list1 = [1, 2, 3, 4, 5]
list2 = 'python'
print random.choice(list1)
print random.choice(list2)

print random.random()

unif = random.uniform(3.99, 4)
print unif

random.seed(10)
print random.random()
random.seed(10)
print random.random()
random.seed(10)
print random.random()

print 'list1:', list1
random.shuffle(list1)
print 'Reshuffled list1: ', list1

str = "this is string example....WOW!!!";

print "str.capitalize() : ", str.capitalize()
sub = 'i'
print 'str.count():', str.count(sub, 0, len(str))


str = 'this is string example...wow!!!'
str = str.encode('base64', 'strict')

print 'Encoded String: ', str
print 'Decoded String: ', str.decode('base64', 'strict')

astr = 'abs'
obj = {astr: 'hello'}
print obj


import time


ticks = time.time()
print ticks
print math.floor(ticks)
print type(math.floor(ticks))
print int(math.floor(ticks))


# 时间戳转时间
localtime = time.localtime(time.time())
print 'local current time : ', localtime
print localtime.tm_year
print localtime.tm_mon
print localtime.tm_mday
print localtime.tm_hour
print localtime.tm_min
print localtime.tm_sec
print localtime.tm_wday
print localtime.tm_yday
print localtime.tm_isdst


localtime = time.asctime(time.localtime(time.time()))
print 'Local current time: ', localtime


import calendar

cal = calendar.month(2015, 1)
print 'calendar:'
print cal

# help(calendar)
# help(eval)
print eval('2 + 3')
print eval("'system' + ' method'")

name = 'shenzp'
room = 73
website = 'shenzp@shen.com'
print 'my name is %s\nmy room is:%d\nmy website is:%s' %(name, room, website)


list = [1, 2, 3, 4]
print list
# print str(list)
print repr(list)

# print str(0.1)
print repr(0.1)

print 'hello'

total = 10

def sum(arg1):
    global total
    total = total + arg1;
    print 'inside:  ', total;
    return total

print sum(10)
print 'outside: ', total

import support

support.print_func('Tom')

from support import print_func
print_func('James')

import sys
print sys.path


import Phone
Phone.Pots()
Phone.G3()
Phone.Isdn()

try:
    fh = open('hello.txt', 'w')
    fh.write('This is my test file for exception handling!')
except IOError:
    print "Error: can,t find file or read data"
else:
    print 'Written content in the file successfully'
    fh.close()