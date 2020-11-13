#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Export_import.py
# Author: tian guang yuan
# Time  : 2020/11/10 9:16
import requests
from hyper.contrib import HTTP20Adapter


# 1、路径-url
Host = 'https://adnet.qq.com'
api_url = f'{Host}/eros/login/user'

header = {
'User-Agent': 'python-requests/2.21.0',
'Accept-Encoding': 'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Cookie': 'PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiIzMDkwMDAyMTQzNzQiLCJpc1N1cGVyVWluS2V5IjoiMCIsImN1c3RvbWVyVXNlcklkU2Vzc2lvbktleSI6IjE4MzM4MDQwIiwib3BlbklkU2Vzc2lvbktleSI6IkI0Qzc4QzVBRUJFQUJENTYzREUxRDRCODhEOTZFNzNFIn0sIm5iZiI6MTYwNDk5ODY5NSwiaWF0IjoxNjA0OTk4Njk1fQ.RR20PaMpXpMA_Aamk8rhadPngnrpYbIHXwBEXmB9xDw; RK=NvbxPBzTMU; _qpsvr_localtk=0.2688100414601151; adnet_li=$1$zylGxik/$tozfVq5Sd9B9lvvHJsQuD/; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_quality_plan_result=1; adnet_sso=TGT-49724-OWYq5GvV1Y3NFiypgN7lLdV.RC3XPxJR3r81dgoP5D0J2jWjVbvbn1U.TSPPZJou; adnet_sso_flag=1; adnet_uin=309000214374; adnet_uname=%E5%86%AF%E9%9B%85%E6%A2%A6; pgv_info=ssid=s190338262; pgv_pvi=6799438848; pgv_pvid=9586900888; pgv_si=s5510458368; ptcz=084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1; ptui_loginuin=1440186482; ts_refer=sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14; ts_uid=5167191916'}

cooki = {
    'RK': 'NvbxPBzTMU',
    'ptcz': '084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1',
    'pgv_pvid': '9586900888',
    'pgv_pvi': '6799438848',
    'pgv_si': 's5510458368',
    '_qpsvr_localtk': '0.2688100414601151',
    'ptui_loginuin': '1440186482',
    'adnet_quality_plan_result': '1',
    'pgv_info': 'ssid=s190338262',
    'ts_uid': '5167191916',
    'ts_refer': 'sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14',
    'adnet_uin': '309000214374',
    'adnet_openId': 'B4C78C5AEBEABD563DE1D4B88D96E73E',
    'adnet_sso_flag': '1',
    'adnet_sso': 'TGT-74133-xcfD7vwyLyXeCYeIhvNlblGkFG89mE2T8AT6Jpl6EiQ1PjdMIySGzZX0An7Xz9E9',
    'PLAY_SESSION':'eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiIzMDkwMDAyMTQzNzQiLCJpc1N1cGVyVWluS2V5IjoiMCIsImN1c3RvbWVyVXNlcklkU2Vzc2lvbktleSI6IjE4MzM4MDQwIiwib3BlbklkU2Vzc2lvbktleSI6IkI0Qzc4QzVBRUJFQUJENTYzREUxRDRCODhEOTZFNzNFIn0sIm5iZiI6MTYwNDk5ODY5NSwiaWF0IjoxNjA0OTk4Njk1fQ.RR20PaMpXpMA_Aamk8rhadPngnrpYbIHXwBEXmB9xDw',
    'adnet_uname': '%E5%86%AF%E9%9B%85%E6%A2%A6',
    'adnet_li': '$1$zylGxik/$tozfVq5Sd9B9lvvHJsQuD/'
    }

sessions = requests.session()
sessions.mount('https://adnet.qq.com/eros/login/user', HTTP20Adapter())
reps = sessions.get(api_url, cookies=cooki, verify=False)
# 代码查看请求头
# print(reps.request.headers)
# 打印响应内容--字符串类型
print(reps.text)









