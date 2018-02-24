# coding=utf8
"""
4-2 如何判断字符串a是否以字符串b开头或结尾

案例：某文件系统目录下游一系列文件，找出其中.ssh和.py的文件

解决方案：使用字符串的str.startswith()和str.endswith()方法，多个匹配时参数使用元组

"""
file = "q.c w.e r.t t.y c.py s.ssh k.jj"
print [name for name in file.split(" ") if name.endswith(('.ssh', '.py'))]