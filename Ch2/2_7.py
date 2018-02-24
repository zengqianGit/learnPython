# coding=utf8
"""
2-4 如何实现用户的历史记录功能（最多n条）

解决方案：使用容量为n的队列(deque)存储；使用pickle将队列对象存入文件实现持久化
"""

from random import randint
from collections import deque
import pickle

N = randint(0, 100)
try:
    d = pickle.load(open('history'))    # 在文件中读取python对象的数据
except:
    d = deque([], 5)


def guess(k):
    if k == N:
        print 'right'
        return True
    if k > N:
        print 'bigger'
    else:
        print 'less'
    d.append(k)
    pickle.dump(d, open('history', 'w'))    # dump()将python对象写入文件
    return False


while True:
    line = raw_input("input a number: ")
    if line.isdigit():
        k = int(line)
        if guess(k):
            break
    elif line == 'h?':
        for i in d:
            print i


# 多个对象按序dump和load
# import pickle
# from collections import deque
#
# d1 = deque(['q','w','e','r','t'], 5)
# d2 = deque(['a','s','d','f','g'], 5)
#
# f1 = file('dumptest.pkl', 'wb')
# pickle.dump(d1, f1, True)
# pickle.dump(d2, f1, True)
# f1.close()
#
# f2 = file('dumptest.pkl', 'rb')
# a1 = pickle.load(f2)
# a2 = pickle.load(f2)
#
# print a1
# print '-' * 20
# print a2