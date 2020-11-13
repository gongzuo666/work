#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : postman.py
# Author: tian guang yuan
# Time  : 2020/11/11 15:11
import requests

url = "http://110.249.209.202:48081/data-import/import-excel-data"

# payload = {}
files = [
  ('file', open('D:/广点通_2020-11-11.csv', 'rb'))
]
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYwNTA4MDEzMSwiaWF0IjoxNjA1MDcyOTMxfQ.wq_yIaA64v8PSlL-WRcCaDLeCZtXV5ow5EByDZ3qhjrt0_O1XdZdhzPjhBVBg1LkzTz9p1HO-f_ncJEqsOK77w',
  'Cookie': 'management-Token=0f1c5ccd-64d5-4433-8003-475e81cd89b7; sidebarStatus=width:%20230px; leftStatus=margin-left:%20230px%3B; translate=transform:translateX(0); username=admin; password=e10adc3949ba59abbe56e057f20f883e; rememberMe=true; siId=1326037773223866369; phone=15100978674; tmId=1326037773282586626; trId=1326036312427474946; tiId=1326037773165146114; storeType=1; storeName=%E6%9C%B1%E6%80%BB%E5%BE%97%E5%BA%97%E9%93%BA; isSetPayPassword=false; realName=%E6%9C%B1%E6%80%BB%E6%80%BB%C2%B7%E6%9C%B1%E6%80%BB%E6%80%BB%E6%9C%B1%E6%80%BB%E6%80%BB%C2%B7%E6%9C%B1%E6%80%BB%E6%80%BB%E6%9C%B1; storeLogoUrl=http://110.249.209.202:46999/static/b/img/1326036312427474946/trader/202011101343022wdgczv9anjp69x9be.png; idCard=511900196910191895; joinPhaseField=HOME; 1605072167000=undefined; 1605072169000=undefined; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYwNTA4MDEzMSwiaWF0IjoxNjA1MDcyOTMxfQ.wq_yIaA64v8PSlL-WRcCaDLeCZtXV5ow5EByDZ3qhjrt0_O1XdZdhzPjhBVBg1LkzTz9p1HO-f_ncJEqsOK77w'
}
# 发送请求
response = requests.post(url, headers=headers, files=files)
# 打印内容
print(response.text)



