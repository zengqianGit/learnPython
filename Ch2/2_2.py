# coding=utf8
"""
2-2 如何为元组中的每个元素命名，提高程序可读性

案例：
学生信息系统中数据为固定格式（名字，年龄，性别，邮箱地址...），学生数量很大时为了减小存储开销，对每个学生信息用元组表示：
{'zq', 16, 'male', 'zq@asd.com'}...访问时，使用index访问会降低程序可读性，如何解决这个问题？

解决方案：
1、定义类似与其他语言的枚举类型（py没有枚举），也就是定义一系列数值常量
2、使用标准库中collections.namedtuple替代内置tuple
"""


# 方案1
NAME, AGE, SEX, EMAIL = xrange(4)
student = ('Jim', 16, 'male', 'jim@qwe.com')
print student[NAME]
# ...


# 方案2
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'Jim@qwe.com')
print s
print s.email
print isinstance(s, tuple)