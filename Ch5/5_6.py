# coding=utf8
"""
5-6 如何使用临时文件

案例：
某项目中，我们从传感器采集数据，每收集到1G数据后，做数据分析，最终只保存分析结果。这样很大的临时数据
如果常驻内存，将消耗大量内存资源，我们可以使用临时文件存储这些临时数据（外部存储）
临时文件不用命名，且关闭后会自动被删除

解决方案：使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile

"""