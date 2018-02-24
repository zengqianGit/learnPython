# coding=utf8
"""
4-1 如何拆分含有多种分隔符的字符串

案例：字符串中包含多种不同的分隔符，如何处理

解决方案：
1、连续使用str.split()方法，每次处理一种分隔符号
2、使用正则表达式的re.split()方法，一次性拆分字符串（推荐）
"""

# 方案2
import re
print re.split(r'[;\\?|]+', str)


# append和extend都仅只可以接收一个参数，append 任意，甚至是tuple，extend 只能是一个列表
# 方案1
str = 'qweqwe;;qr\qw?rqqeqrq|qwerf'
sign = [';', '\\', '?', '|']
s = [str]
for sn in sign:
    t = []
    map(lambda x: t.extend(x.split(sn)), s)
    s = t
print [x for x in s if x] # 过滤空字符串
