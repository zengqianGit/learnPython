# coding=utf8
"""
2-5 如何快速找到多个字典中的公共键(key)

解决方案：使用集合(set)的交集操作
step1、使用字典的viewkeys()方法，得到一个字典的keys的集合
step2、使用map函数得到所有字典的keys的集合
step3、使用reduce函数，取所有字典的keys的集合的交集
"""

from random import randint, sample

print sample('abcdefg', randint(3,6))
# sample(seq, n) 从序列seq中选择n个随机且独立的元素；
s1 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
s2 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
s3 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}

# 字典较少时可以使用viewkeys()
res1 = s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
print res1

# 字典较多时
res2 = reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
# reduce( func, [1, 2,3] ) = func( func(1, 2), 3)
# reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）与下一个元素一同执行一个二元的func函数。
print res2