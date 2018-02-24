# coding=utf8
"""

2-6 如何让字典保持有序

案例：字典格式为{名字:(名次, 时间)}，需按排名顺序依次打印选手成绩，如何实现

解决方案：使用OrderedDict替代内置字典Dict，依次将选手成绩存入
"""

from time import time
from random import randint
from collections import OrderedDict

start = time()
player = list('QWERTYUI')
d = OrderedDict()

for i in range(8):
    raw_input()
    end = time()
    p = player.pop(randint(0, 7 - i))
    print p, 1 + i, end - start,
    d[p] = (1 + i, end - start)

print
print '-' * 20
for k in d:
    print k, d[k]
