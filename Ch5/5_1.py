# coding=utf8
"""
5-1 如何读写文本文件

解决方案：字符串的语义发生了变化：str(py2) -> bytes(py3)；unicode(py2) -> str(py3)
1、python2.x：写入文件前对unicode编码，读入文件后对二进制字符串编码
2、python3.x：open函数制定't'的文本模式，encoding制定编码格式、

"""
# python2
f = open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('gbk'))
f.close()
f = open('py2.txt', 'r')
t = f.read()
print t
print t.decode('gbk')

# python3
# f = open('py3.txt', 'rt', encoding='utf8')
# f.write('你好')
# f.close()
# f = open('py3.txt', 'rt', encoding='utf8')
# s = f.read()
# print s