# coding=utf8
"""
3-6 如何在一个for语句中迭代多个可迭代对象

案例：
1、某班期末成绩，语文、数学、英语分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分（并行）
2、某年级有4个班，某次考试每班成绩分别存储在4个列表中，依次迭代每个列表，统计全学年成绩高于90分人数（串行）

解决方案：
1、并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组（索引的方法有局限性，如生成器就不支持）
2、串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接
"""
# 并行
from random import randint

chinese = [randint(0, 100) for _ in xrange(40)]
math = [randint(0, 100) for _ in xrange(40)]
english = [randint(0, 100) for _ in xrange(40)]

total = []
for c, n, e in  zip(chinese, math, english):
    total.append(c + n + e)
# print total


# 串行
from itertools import chain


e1 = [randint(0, 100) for _ in xrange(40)] 
e2 = [randint(0, 100) for _ in xrange(40)]
e3 = [randint(0, 100) for _ in xrange(40)]
e4 = [randint(0, 100) for _ in xrange(40)]
i = [i for i in chain(e1, e2, e3, e4) if i > 90]
print len(i)
