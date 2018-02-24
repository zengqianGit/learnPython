# coding=utf8
"""
6-3 如何解析简单的xml文档

案例：xml是一种十分常用的标记性语言，可提供统一的方法来描述应用程序的结构化数据:
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
python中如何解析xml文档

解决方案：使用标准库中的xml.etree.ElementTree，其中的parse函数可以解析xml文档


"""