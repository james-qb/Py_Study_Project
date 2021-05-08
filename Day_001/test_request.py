#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 8:38
# @Author  : qiubin
# @File    : test_request.py
# @Software: PyCharm
import requests

new_dict = {}


def get_key_value(temp_dict):
    for skey, svalue in temp_dict.items():
        if type(svalue) != dict:
            print(skey + ': ' + str(svalue))
        else:
            get_key_value(svalue)


url = "https://apiuat.cresz.com.cn/openapi/?model=app"

headers = {
    'Content-Type': 'application/json;charset=utf-8'
}

data = {
    "REQUEST": {
        "API_ATTRS": {
            "Api_ID": "pcc.pccsys.pccmbr.getUser",
            "Api_Version": "1.0.0",
            "App_ID": "5000000115WR",
            "App_Sub_ID": "5000000115WR",
            "App_Token": "aa11bf4c-b16f-4970-a2bd-70817cfb0352",
            "App_Version": "4.1.3",
            "Divice_ID": "3d6823mf5wx",
            "Divice_Version": "iPhone 7 Plus",
            "OS_Version": "iOS 10.0.1",
            "Partner_ID": "50000000",
            "Sign": "C911A60445ACBD9BE392E4FD809B589F",
            "Time_Stamp": "2021-04-25 17:20:43:253",
            "User_Token": ""
        },
        "REQUEST_DATA": {
            "accessToken": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmZjgwODE4MTc1Zjk1MzRjMDE3NWY5NWUwM2FlMDAwMyIsImlhdCI6MTYxMDM0OTkwMCwic3ViIjoiMTMzMTY5NTEwOTAifQ.ZIASamUtOXIPI0MlRSX4ePN9ITKsVQjUAnksdouR1JQ",
            "buUserNo": "100000003000104", "channelId": "APP"}
    }
}
req = requests.request("POST", url, headers=headers, json=data)
return_code = req.status_code
return_json = req.json()
get_key_value(return_json)
