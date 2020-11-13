#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : aa.py
# Author: tian guang yuan
# Time  : 2020/11/12 9:57
import requests
import json
from hyper.contrib import HTTP20Adapter
import datetime

# 今天的日期
today = datetime.date.today()
# 昨天的日期
yesterday = today - datetime.timedelta(days=1)
# 4、路径-url
print("开始从优量汇系统->广告数据->下载报告")
api_url = 'https://adnet.qq.com/report/getReportTableData'
header = {
    ':method': 'POST',
    ':authority': 'adnet.qq.com',
    ':scheme': 'https',
    ':path': '/report/getReportTableData',
    'content-length': '231',
    'accept': '*/*',
    'time': '1604999382657',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'sign': 'd3f37645e01b341fd9040f5516f9523e',
    'content-type': 'application/json',
    'origin': 'https://adnet.qq.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://adnet.qq.com/report/list',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Cookie': 'RK=NvbxPBzTMU; ptcz=084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1; pgv_pvid=9586900888; pgv_pvi=6799438848; pgv_si=s5510458368; _qpsvr_localtk=0.2688100414601151; ptui_loginuin=1440186482; adnet_quality_plan_result=1; pgv_info=ssid=s190338262; ts_uid=5167191916; ts_refer=sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14; adnet_uin=309000214374; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_sso_flag=1; adnet_sso=TGT-24464-rqq.C28pz.QG.A1YynUD.C8ht62dQvHc73Qxw.p5haxj0Feq6lDISN6U5gzxzR.m; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiIzMDkwMDAyMTQzNzQiLCJpc1N1cGVyVWluS2V5IjoiMCIsImN1c3RvbWVyVXNlcklkU2Vzc2lvbktleSI6IjE4MzM4MDQwIiwib3BlbklkU2Vzc2lvbktleSI6IkI0Qzc4QzVBRUJFQUJENTYzREUxRDRCODhEOTZFNzNFIn0sIm5iZiI6MTYwNTE0Njc3MCwiaWF0IjoxNjA1MTQ2NzcwfQ.qo2EyPVQeH-J6uMe4lnaPWqnTITsxywnik2IyfSyaMg; adnet_uname=%E5%86%AF%E9%9B%85%E6%A2%A6; adnet_li=$1$YQHbxZ/3$MeFDEiCgHoETqKbF/34qO0'}

# 2、参数
payload = json.dumps({
    "memberId": 309000214374,
    "startDate": f"{yesterday}",
    "endDate": f"{yesterday}",
    "placementType": [],
    "medium": [],
    "placement": [],
    "pageIndex": 0,
    "pageSize": 20,
    "orderByClause": "ReportDay desc",
    "selectAllMedium": "false",
    "selectAllPlacement": "false"
})
sessions = requests.session()
sessions.mount('https://adnet.qq.com/report/getReportTableData', HTTP20Adapter())
reps = sessions.post(api_url, data=payload, headers=header, verify=False)
print(reps.json())
