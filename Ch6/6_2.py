# coding=utf8
"""
6-2 如何读写json数据

案例：在web应用中常用JSON格式传输数据，例如我们利用Baidu语音识别服务做语音识别，
将本地音频数据post到Baidu语音识别服务器，服务器响应结果为json字符串：
{
    "err_no": 0,
    "err_msg": "success.",
    "corpus_no": "15984125203285346378",
    "sn": "481D633F-73BA-726F-49EF-8659ACCC2F3D",
    "result": ["北京天气"]
}
在python中如何读写json数据

解决方案：使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写

"""