#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 14:42
# @Author  : qiubin
# @File    : test_post.py
# @Software: PyCharm
import requests

# url = "http://httpbin.org/post"
# data = {"key1": "value1", "key2": "value2"}
# headers = {"Content-type": "application/x-www-form-urlencoded"}
# r = requests.post(url=url, data=data, headers=headers)
# print(r.text)

import requests

files = {'file': open(r'D:\1.txt', 'rb')}
url = "http://httpbin.org/post"
fields = {"field0": "value", "field1": "value"}  # 删掉fields效果一样
r = requests.post(url=url, data=fields, files=files)
print(r.status_code)
print(r.text)

import requests
url = r'http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png'
path = 'D://2.jpg'
r = requests.get(url=url, stream=True)
print(r.status_code)
with open(path, 'wb') as f:
    f.write(r.content)
