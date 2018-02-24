# coding=utf8
"""
5-3 如何设置文件的缓冲

案例：将文件内容写入到硬件设备时，使用系统调用，这类I/O操作的时间很长，为了减少I/O操作的次数，文件通常使用缓冲区
（有足够多的数据才进行系统调用）。文件的缓冲行为分为全缓冲，行缓冲，无缓冲。如何设置python中文件对象的缓冲行为？

解决方案：
1、全缓冲：open函数的buffering设置为大于1的证书n，n为缓冲区大小
2、行缓冲：buffering设置为1
3、无缓冲：buffering设置为0

"""
f = open('53.txt', 'w', buffering=2048)
f = open('53.txt', 'w', buffering=1)
f = open('53.txt', 'w', buffering=0)

f.write('abc')