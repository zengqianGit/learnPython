# coding=utf8
"""
4-4 如何将多个小字符串拼接成一个大的字符串

解决方案：
1、使用str1 + str2。缺点：在字符串很大时，会创建和释放大量临时字符串，开销巨大
2、使用str.join()。推荐
"""
print ';'.join(['asd','cvb','fgh','qwe'])
print ''.join(['asd','cvb','fgh','qwe'])

# 当列表里有int有string时
l = ['asd', 123, 45, 'ert']
# print ''.join([str(x) for x in l]) # 需要生成一个新列表，当原列表大时开销大
print (str(x) for x in l)           # 这是一个生成器
print ''.join(str(x) for x in l)
