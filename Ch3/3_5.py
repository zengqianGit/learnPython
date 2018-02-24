# coding=utf8
"""
3-5 如何对迭代器做切片操作

案例：有某个文本文件，我们想读取其中某范围的内容如100~300行，python中的文件是可迭代对象，是否可以使用类似列表切片的方式得到
一个100~300行文件内容的生成器？
TypeError:'file' object has no attribute '__getitem__'

解决方案：使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器
"""
from itertools import islice

f = open('../Ch2/test')

for x in islice(f, 100):
    print x  # 注意islice会消耗f，切片及其前边的内容会被从f中抛出

# islice(f, 100)        前100行
# islice(f, 100, 300)   100~300行
# islice(f, 100, None)  100行到最后
# islice(f, 100, -100)  异常，islice在读取完整个文本前无法知道-100的位置