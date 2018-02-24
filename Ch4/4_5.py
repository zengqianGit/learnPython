# coding=utf8
"""
4-5 如何对字符串进行左，右，居中对齐

案例：以工整的格式将某内容输出，如何处理？

解决方案：
1、使用str.ljust()、str.rjust()和str.center()进行对齐
2、使用format()方法，'<' '>' '^' 分别代表左、右、居中对齐
"""

d = {
    'qweqwrqw': 100.0,
    'ertfg': 10.0,
    'hfmg': 150.0,
    'eeopopo': 200.0,
    'gh': 105.0,
}
w = max(map(len, d))
for k in d:
    print k.ljust(w), ': ', d[k]
print "-" * 30
for k in d:
    print format(k, '^'+str(w)), ": ", d[k]