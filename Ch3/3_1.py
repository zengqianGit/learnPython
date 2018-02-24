# coding=utf8
"""
3-1 如何实现可迭代对象和迭代器对象（1）

什么对象是可迭代对象？
> 拥有__iter__或__getitem__接口（说明这是一个seq）的对象。由可迭代对象得到迭代器（通过iter()和reversed()）
"""
l = [1,2,3,4]
t = iter(l)

# 超出范围会抛出StopIteration异常
for i in xrange(len(l)):
    print t.next()