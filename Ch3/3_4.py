# coding=utf8
"""
3-4 如何进行反向迭代以及如何实现反向迭代

解决方案：iter(l)得到正向迭代器，reversed(l)得到反向迭代器
实现反向迭代协议的__reversed__方法，它返回一个反向迭代器
"""


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in FloatRange(1, 10, 0.5):
    print x




# 如何反向迭代一个列表
# l = [1, 2, 3, 4, 5]
# l.reverse() # 会改变原列表
# l[::-1]     # 生成同等大小的新列表，造成浪费
# reversed(l) # 该内置函数得到列表的反向迭代器，推荐使用。iter(l)得到正向迭代器
# for i in reversed(l):
#     print i
