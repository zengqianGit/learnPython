# coding=utf8
"""
5-2 如何处理二进制文件

案例：wav是一种音频文件的格式，音频文件为二进制文件。wav文件由头部信息和音频采样数据构成。
前44个字节为头部信息，包括声道数、采样频率、PCM位宽等等。

解决方案：
step1、open函数以二进制模式打开文件，指定mode参数为'b'
step2、二进制数据可以用readinto，读入到提前分配好的buffer中，便于数据处理
step3、解析二进制数据可以使用标准库中的struct模块的unpack方法

"""
import struct
f = open('q.wav', 'rb')
info = f.read(44)
# print struct.unpack('h', info[22:24])
# print struct.unpack('i', info[24:28])
# print struct.unpack('h', info[34:36])

import array
data_size = f.seek(0, 2) # fileObject.seek(offset[, whence])
                            # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
                            # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
                            #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
data_size = f.tell() - 44 / 2 # 2是宽度，由struct.unpack('h', info[22:24])决定
buf = array.array('h', (0 for _ in xrange(data_size))) # 第二个参数是一个生成器参数
f.seek(44)
f.readinto(buf)
for i in xrange(data_size): buf[i] /= 8 # 音量全部减小
f2 = open('q2.wav', 'wb')
f2.write(info)
buf.tofile(f2) # 将音频采样数据写入文件




