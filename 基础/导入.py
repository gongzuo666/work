#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 导入.py
# Author: tian guang yuan
# Time  : 2020/11/11 10:52

import requests
import json
def login(name, pwd):
    # 路径-url
    url = 'http://110.249.209.202:48081/auth/login'
    # 请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Content-Type': 'application/json'
        }

    # 请求参数
    payload = json.dumps({"username": name, "password": pwd})
    # 发送请求
    reps = requests.post(url, data=payload, headers=header)
    # 打印内容
    return reps.json()['token']


def filename(name):
    # 路径-url
    api_url = 'http://110.249.209.202:48081/data-import/import-excel-data'
    token = login("admin", "e10adc3949ba59abbe56e057f20f883e")
    # 请求头
    header = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Cookie': 'management-Token=0f1c5ccd-64d5-4433-8003-475e81cd89b7; sidebarStatus=width:%20230px; leftStatus=margin-left:%20230px%3B; translate=transform:translateX(0); username=admin; password=e10adc3949ba59abbe56e057f20f883e; rememberMe=true; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYwNTA2NzgzOSwiaWF0IjoxNjA1MDYwNjM5fQ.zZ6fwID_QniedKun6Hg2FT3iOcgn2DN4R4BWU2VDfHSDiUs1FZZLA9frjWe7ugNIkEkSOPdDSlow5maB7c3h0g'
        }
    f = open(name, 'rb')
    # 请求参数
    files = [('file', f)]
    # 发送请求
    reps = requests.post(api_url, files=files, headers=header)
    # 打印内容
    f.close()
    return reps.text
if __name__ == '__main__':
    # print(login("admin", "e10adc3949ba59abbe56e057f20f883e"))
    print(filename("D:/广点通_2020-11-11.csv"))



