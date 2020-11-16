#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Export_import.py
# Author: tian guang yuan
# Time  : 2020/11/10 9:16
import time, json, os, csv, datetime
from selenium import webdriver
import requests
from hyper.contrib import HTTP20Adapter
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 今天的日期
today = datetime.date.today()
# 昨天的日期
yesterday = today - datetime.timedelta(days=1)
# 创建文件对象
file = f'D:/广点通_{today}.csv'

# 定义显示等待函数
def webElementWait(driver, timeout,lo_time,by_locate,locate):
    """

    :param driver: 浏览器驱动对象
    :param timeout: 最大等待时间
    :param lo_time: 轮询时间
    :param by_locate: 定位方法
    :param locate: 元素定位表达式
    :return:
    """
    # 每隔 0.5 秒检查一次，最多等待 10 秒
    ele = WebDriverWait(driver, timeout, lo_time).until(
        EC.visibility_of_element_located(
            (by_locate, locate)
        )
    )
    return ele

def ylh_login(name,pwd):
    # 这两行是实现无界面的关键代码
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')  # 实现静默模式，在电脑上不显示页面
    option.add_argument('window-size=1300,1300')  # 设置浏览器窗口大小
    option.add_argument('--start-maximized')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    # 访问网址
    driver.get("https://sso.e.qq.com/login/hub?sso_redirect_uri=https%3A%2F%2Fe.qq.com%2Fdev%2Flogin%3F&service_tag=14")
    # 设置为全屏展示
    driver.maximize_window()
    # 刷新页面
    driver.refresh()
    # 切换到这个内嵌网页
    eIframe = webElementWait(driver, 10, 0.5, By.CSS_SELECTOR, "#qqLoginFrame")
    driver.switch_to.frame(eIframe)
    eleIframe = webElementWait(driver, 10, 0.5, By.CSS_SELECTOR, "#ptlogin_iframe")
    driver.switch_to.frame(eleIframe)
    webElementWait(driver, 10, 0.5, By.CSS_SELECTOR, "#switcher_plogin").click()
    # 2 输入用户名,密码
    driver.find_element_by_css_selector(".inputstyle").send_keys(name)
    driver.find_element_by_css_selector(".inputstyle.password").send_keys(pwd)
    driver.find_element_by_css_selector(".btn").click()
    # 检查
    try:
        aa = webElementWait(driver, 10, 0.5, By.CSS_SELECTOR, "#page > div > div.frame-head a > span.text")
        if aa.text == "优量汇":
            print("登录成功，关键信息获取成功")
        return driver.get_cookies()[-2]['value']
    except Exception as e:
        print(e)

def export_report(adnet_sso):
    # -----------------------------------------------接口数据获取--------------------------------------------
    # adnet_sso = ylh_login()
    print("开始从优量汇系统->广告数据->下载报告")
    # 1. 打开文件写入
    with open(file, 'w', encoding='UTF-8', newline='') as f:
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 3. 构建列表头
        csv_writer.writerow(["时间", "广告展示数", "点击量", "预计收入", "千次展示收益", "点击率"])

        # 路径-url
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
            'Cookie': f'RK=NvbxPBzTMU; ptcz=084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1; pgv_pvid=9586900888; pgv_pvi=6799438848; pgv_si=s5510458368; _qpsvr_localtk=0.2688100414601151; ptui_loginuin=1440186482; adnet_quality_plan_result=1; pgv_info=ssid=s190338262; ts_uid=5167191916; ts_refer=sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14; adnet_uin=309000214374; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_sso_flag=1; adnet_sso={adnet_sso}; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiIzMDkwMDAyMTQzNzQiLCJpc1N1cGVyVWluS2V5IjoiMCIsImN1c3RvbWVyVXNlcklkU2Vzc2lvbktleSI6IjE4MzM4MDQwIiwib3BlbklkU2Vzc2lvbktleSI6IkI0Qzc4QzVBRUJFQUJENTYzREUxRDRCODhEOTZFNzNFIn0sIm5iZiI6MTYwNDk5ODY5NywiaWF0IjoxNjA0OTk4Njk3fQ.u-JYqvuSa-czzZ4AG-NL9Nu6polDN6Qdc_B4qSsgs6o; adnet_uname=%E5%86%AF%E9%9B%85%E6%A2%A6; adnet_li=$1$oPdD32MW$FuDaeprKLq9BE70/C/YTL0; ts_last=adnet.qq.com/report/list'}

        # 参数
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
        reps = sessions.post(api_url, data=payload, headers=header)
        if (reps.json()['data']['size']) != 0:
            # 打印响应内容
            list1 = reps.json()['data']['entities']
            # 循环打印
            for lis in list1:
                # 获取日期
                formatDate = lis['formatDate']
                # 广告展示量
                formatPV = lis['formatPV']
                # 点击量
                formatClick = lis['formatClick']
                # 预计收入
                formatRevenueAfterSharingByYuan = lis['formatRevenueAfterSharingByYuan']
                # 千次展示收益
                formatECPM = lis['formatECPM']
                # 点击率
                formatClickRate = lis['formatClickRate']

                csv_writer.writerow([f"{formatDate}", f"{formatPV}", f"{formatClick}", f"{formatRevenueAfterSharingByYuan}", f"{formatECPM}", f"{formatClickRate}"])
                # 5. 关闭文件
                # f.close()
                yesterday_data = f'日期:{formatDate} | 广告展示量:{formatPV} | 点击量:{formatClick} | 预计收入:{formatRevenueAfterSharingByYuan} | 千次展示收益:{formatECPM} | 点击率:{formatClickRate}'
            return f"昨日{yesterday}数据明细：{yesterday_data}"
        else:
            return f"昨日{yesterday}数据为空"

# -----------------------------登录后台海量引擎广告投放后台管理系统-------------------------------------------
# 封装登录
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

# 封装导入函数
def filename(name):
    print("开始向海量引擎广告投放后台管理系统->数据收益->导入数据")
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
    # assert reps.text[0:4] == "导入成功"
    if reps.text[0:4] == "导入成功":
        return reps.text
    else:
        return f"导入失败：{reps.text}"

def main():
    ylh = ylh_login("1440186482", "hebeihailiang1234")
    if ylh != None:
        yesterdayData = export_report(ylh)
        print(yesterdayData)
        if yesterdayData == f"昨日{yesterday}数据为空":
            print("不进行导入")
            os.remove(file)
        else:
            print(filename(file))
            os.remove(file)
    else:
        print("登录失败，关键信息未获取")

if __name__ == '__main__':
    # print(export_report())
    # print(filename(file))
    # os.remove(file)
    main()
    # print(ylh_login())
    # BlockingScheduler
    # scheduler = BlockingScheduler()
    # job = scheduler.add_job(main, 'cron', day_of_week='1-6', hour='*', minute=47)
    # scheduler.start()
    # job.remove()



