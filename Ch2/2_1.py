# coding=utf8
"""
2-1 如何在列表，字典，集合中根据条件筛选数据

解决方案：
    1、遍历
    2、Filter函数
    3、解析（速度最快）
"""

# 列表解析：[x for x in data if x >= 0]
from random import randint
data = [randint(-10, 10) for _ in xrange(10)]
# data = filter(lambda x: x >= 0, data)
dd = [x for x in data if x >=0 ]
print dd

# 字典解析：{k:v for k,v in d.iteritems() if v > 90}
d = {x: randint(60, 100) for x in xrange(1, 21)}
d = {k: v for k, v in d.iteritems() if v > 90}
print d

# 集合解析：{x for x in s if x % 3 == 0}
s = set(data)
s = {x for x in s if x % 3 == 0}
print s

