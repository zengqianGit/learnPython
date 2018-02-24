# coding=utf8
"""
2-4 如何根据字典中值的大小，对字典中的项排序

案例：某班英语成绩以字典形式存储（姓名:成绩），根据成绩高低，计算学生排名

解决方案：使用内置函数sorted
1、利用zip将字典数据转化元组
2、传递sorted函数的key参数
"""
# 方案1
from random import randint
d = {x: randint(0, 10) for x in 'xyzabc'}
print d
print iter(d)
d = sorted(d)
print iter(d)   # 排序后value丢失

d1 = {x: randint(0, 10) for x in 'xyzabc'}
d2 = zip(d1.values(), d1.keys())
# zip(list1, list2) = map(None, list1, list2)
d3 = zip(d1.itervalues(), d1.iterkeys())    # 内存优化
print d1
d3 = sorted(d3)
print d3


# 方案2
d4 = sorted(d1.items(), key=lambda x: x[1])
print d4