# coding=utf8
"""
2-2 如何统计序列中元素的出现频度

案例：
1、某随机序列中，找到出现次数最高的3个元素，他们出现次数是多少？
2、对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，他们出现次数是多少

解决：使用collections.Counter对象，most_common(int)
"""

# 案例1
from random import randint
from collections import Counter
data = [randint(0, 10) for _ in xrange(30)]
print data
dic = dict.fromkeys(data, 0)
print dic
for i in data:
    dic[i] += 1
print dic
d = Counter(dic)
d = d.most_common(3)
print d


# 案列2
import re
txt = open("test").read()
c = Counter(re.split('\W+', txt))
c = c.most_common(10)
print c