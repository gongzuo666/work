#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : bb.py
# Author: tian guang yuan
# Time  : 2020/11/19 17:32
from report.Export_import import ylh_login
import requests
import json

adnet_sso = ylh_login("1440186482", "hebeihailiang1234")
print(adnet_sso)

url = "https://adnet.qq.com/eros/report/report_table_data"

payload=json.dumps({"start_date":"2020-11-27","end_date":"2020-11-29","biz_filter":{"medium":[1110722686,1110952771,1111021172],"placement_type":["Native","SplashScreen"],"placement":["1081736795574379","3031138640024336","3071042204294838","4041533735375386","4061640225204002","5091936337348463","6011337367442318","6031931400412292","7021838308686202","7091747206506189","8021646276006271","9071133430809129"]},"group_by":["report_day"],"order_by":"","page":1,"page_size":20})
headers = {
  'authority': 'adnet.qq.com',
  'accept': 'application/json',
  'time': '1606786049445',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
  'sign': 'c4f97f92d1a6f3dbf0056010cbd6f547',
  'content-type': 'application/json',
  'origin': 'https://adnet.qq.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://adnet.qq.com/report/list',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': f'RK=NvbxPBzTMU; ptcz=084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1; pgv_pvid=9586900888; pgv_pvi=6799438848; ptui_loginuin=1440186482; adnet_quality_plan_result=1; ts_uid=5167191916; ts_refer=sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14; pgv_si=s1136173056; _qpsvr_localtk=0.6917714785953393; adnet_uin=309000214374; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_sso_flag=1; adnet_sso={adnet_sso}; adnet_uname=%E6%B2%B3%E5%8C%97%E6%B5%B7%E9%87%8F%E5%BC%95%E6%93%8E%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; adnet_li=$1$fdsffdfd$MdN6FVvND8zla1ma.QN0k/; ts_last=adnet.qq.com/settlement/list; adnet_uin=309000214374; adnet_uname=%E6%B2%B3%E5%8C%97%E6%B5%B7%E9%87%8F%E5%BC%95%E6%93%8E%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_li=$1$fdsffdfd$MdN6FVvND8zla1ma.QN0k/; adnet_sso_flag=1'
}

reps = requests.post(url, headers=headers, data=payload)
print(reps.text)
# print(reps.json()['data']['list'])
# lists = len(reps.json()['data']['list'])
# print(lists)
# if lists >= 1:
#     for one in range(lists):
#         pv_data = reps.json()['data']['list'][one]
#         # 打印响应内容
#         request_count = pv_data['request_count']
#         print(request_count)
    # # 循环打印
    # for lis in list1:
    #     # 获取日期
    #     formatDate = lis['formatDate']
    #     # 广告展示量
    #     formatPV = lis['formatPV']
    #     # 点击量
    #     formatClick = lis['formatClick']
    #     # 预计收入
    #     formatRevenueAfterSharingByYuan = lis['formatRevenueAfterSharingByYuan']
    #     # 千次展示收益
    #     formatECPM = lis['formatECPM']
    #     # 点击率
    #     formatClickRate = lis['formatClickRate']

# else:
#     print("昨日{yesterday}数据为空")
