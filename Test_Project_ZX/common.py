#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 15:00
# @Author  : qiubin
# @File    : common.py
# @Software: PyCharm
import requests

url = "http://www.baidu.com/s?"

payload = {}
params = {
    'ie': 'utf-8',
    'wd': '中国'
}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
  (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
  'Cookie': 'BIDUPSID=DFF97F4A43B1B86895D78022DE5B1C68; PSTM=1594696578; \
  BAIDUID=DFF97F4A43B1B86805C7868F3E819856:FG=1; delPer=0; BD_CK_SAM=1; PSINO=7;\
   H_PS_PSSID=1420_31326_32139_31660_32045_32230_32257; BDSVRTM=14'
}

response = requests.request("GET", url, headers=headers, params=params)
print(response.url)

print(response.text)
