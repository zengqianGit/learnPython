# coding=utf8
"""
3-3 何如使用生成器函数实现可迭代对象

案例：实现一个可迭代对象的类，它能迭代出给定范围内的所有素数

解决方案：将该类的__iter__方法实现成生成器函数，每次yield返回一个素数

生成器与迭代器：
生成器(generator)是一种用普通函数语法定义的迭代器。但是，跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，
更简单点理解生成器就是一个迭代器。在 Python 中，可以认为使用了 yield 的函数被称为生成器。在调用生成器运行的过程中，每次遇到
yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。并在下一次执行 next() 方法时从当前位置继续运行。
"""
from time import time


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k / 2 + 1):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

s = time()
c = 0
for i in PrimeNumbers(0, 1000):
    print i,
    c += 1
e = time()
print
print c
print e-s

# 2 3 4 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# def f():
#     print 'in f(), 1'
#     yield 1
#
#     print 'in f(), 2'
#     yield 2
#
#     print 'in f(), 3'
#     yield 3
#
# g = f()
# print g.next()
# print g.next()
# print g.next()
# print g.next()  # StopIteration
#
# for i in g:
#     print i
#
# print g.__iter__() is g # 验证生成器对象是可迭代对象

