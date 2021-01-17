#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xiayan
@file: cookie_add.py
@time: 2020/5/22 20:00
@desc:
'''
import json

#  https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F
cookies = '''M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000061%26fid%3D4397644828677472%26oid%3D4397644828677472; expires=Thu, 25-Jul-2019 02:57:05 GMT; Max-Age=600; path=/; domain=.weibo.cn; HttpOnly'''
dict = {}
cookies = cookies.split(";")
for cookie in cookies:
    dict[cookie.split("=")[0]] = cookie.split("=")[-1]

print(json.dumps(dict))
