# coding=utf8
"""
4-6 如何去掉字符串中不需要的字符

解决方案：
1、字符串strip()，lstrip()，rstrip()方法去掉字符串两端字符
2、删除单个固定位置的字符，可以使用切片 + 拼接的方式
3、字符串的replace()方法或正则表达式re.sub()删除任意位置字符
4、字符串translate()方法，可以同时删除多种不同字符。str和unicode各有一个，目的相同用法不同
"""
# 方案1
# s = '   qwe  rty   '
# print s
# print s.strip()
# print s.lstrip()

# 方案2
# s1 = 'qwe:123'
# print s1[:3]+s1[4:]

# 方案3
# s = '\tasd\tqwe\r\nads'
# print s.replace('\t', '')    # 只能替换一种
# import re
# print re.sub('[\t\r\n]', '', s)

# 方案4
# s = 'asd213123qwe'
# s1 = '\tasd\t qwe\r\nads'
# s2 = '   qwe  rty   '
# import string
# string.maketrans('asdqwe', 'qweasd')
# print s.translate(string.maketrans('asdqwe', 'qweasd'))
# print s1.translate(None, '\t \r\n')
# print s1.translate(None, '\t\r\ n')
# print s2.translate(None, ' ')

# 去掉unicode中拼音的音调
s = u'ni\u0301 ha\u030co'
print s
print s.translate({0x0301: None})
print s.translate(dict.fromkeys([0x0301, 0x030c]))