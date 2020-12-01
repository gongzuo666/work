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
ob_name = f'D:/广点通_{today}.csv'

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
        # return driver.get_cookies()
    except:
        print("遇到了错误，可能元素不稳定或网络问题")

# -----------------------------------------------接口数据获取--------------------------------------------

def export_report(adnet_sso):
    print("开始从优量汇系统->广告数据->下载报告")
    # 1. 打开文件写入
    with open(ob_name, 'w', encoding='UTF-8', newline='') as f:
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 3. 构建列表头
        csv_writer.writerow(["日期", "媒体名称", "媒体ID", "广告位类型", "广告位名称", "广告位ID", "预估收入(元)", "千次展示收入(元)", "广告位请求量", "广告位返回量", "广告请求量", "广告返回量", "曝光量", "点击量", "广告位填充率", "广告位曝光率",	"点击率", "广告填充率", "广告曝光率", "点击成本(元)"
])

        # 路径-url
        url = 'https://adnet.qq.com/eros/report/report_table_data'

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
            'cookie': f'RK=NvbxPBzTMU; ptcz=084a03e673f30cca09d5641ac05b568029d44746d68457f5a57fb785ee1383b1; pgv_pvid=9586900888; pgv_pvi=6799438848; ptui_loginuin=1440186482; adnet_quality_plan_result=1; ts_uid=5167191916; ts_refer=sso.e.qq.com/login/hub%3Fsso_redirect_uri%3Dhttps%3A//adnet.qq.com%26service_tag%3D14; pgv_si=s1136173056; _qpsvr_localtk=0.6917714785953393; adnet_uin=309000214374; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_sso_flag=1; adnet_sso={adnet_sso}; pgv_info=ssid=s4255688433; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiIzMDkwMDAyMTQzNzQiLCJpc1N1cGVyVWluS2V5IjoiMCIsImN1c3RvbWVyVXNlcklkU2Vzc2lvbktleSI6IjE4MzM4MDQwIiwib3BlbklkU2Vzc2lvbktleSI6IkI0Qzc4QzVBRUJFQUJENTYzREUxRDRCODhEOTZFNzNFIn0sIm5iZiI6MTYwNjc4NTkzNiwiaWF0IjoxNjA2Nzg1OTM2fQ.yGdsGvpHbPMlMJcanYK2TKDUVv55Q8ndqvO4_X3I0pY; adnet_uname=%E6%B2%B3%E5%8C%97%E6%B5%B7%E9%87%8F%E5%BC%95%E6%93%8E%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; adnet_li=$1$fdsffdfd$MdN6FVvND8zla1ma.QN0k/; ts_last=adnet.qq.com/settlement/list; adnet_uin=309000214374; adnet_uname=%E6%B2%B3%E5%8C%97%E6%B5%B7%E9%87%8F%E5%BC%95%E6%93%8E%E7%BD%91%E7%BB%9C%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; adnet_openId=B4C78C5AEBEABD563DE1D4B88D96E73E; adnet_li=$1$fdsffdfd$MdN6FVvND8zla1ma.QN0k/; adnet_sso_flag=1'
        }
        # 参数
        payload = json.dumps({"start_date":f"{yesterday}","end_date":f"{yesterday}","biz_filter":{"medium":[1110722686,1110952771,1111021172],"placement_type":["Native","SplashScreen"],"placement":["1081736795574379","3031138640024336","3071042204294838","4041533735375386","4061640225204002","5091936337348463","6011337367442318","6031931400412292","7021838308686202","7091747206506189","8021646276006271","9071133430809129"]},"group_by":["report_day","media_id","placement_type","placement_id"],"order_by":"","page":1,"page_size":20})

        # 发送请求
        reps = requests.post(url, headers=headers, data=payload)

        # 广告数据列表数据条数
        lists = len(reps.json()['data']['list'])
        # 如果大于等于1执行for循环
        if lists >= 1:

            for one in range(lists):
                pv_data = reps.json()['data']['list'][one]
                # 日期
                report_day = pv_data['report_day']
                # 媒体名称
                medium_name = pv_data['medium_name']
                # 媒体ID
                media_id = pv_data['media_id']
                # 广告位类型
                placement_type = pv_data['placement_type']
                # 广告位名称
                placement_name = pv_data['placement_name']
                # 广告位ID
                placement_id = pv_data['placement_id']+'\t'
                # 预故收入
                revenue = pv_data['revenue']
                # 千次展示收入(元)
                ecpm = pv_data['ecpm']
                # 广告位请求量
                request_count = pv_data['request_count']
                # 广告位返回量
                return_count = pv_data['return_count']
                # 广告请求量
                ad_request_count = pv_data['ad_request_count']
                # 广告返回量
                ad_return_count = pv_data['ad_return_count']
                # 曝光量
                pv = pv_data['pv']
                # 点击量
                click = pv_data['click']
                # 广告位填充率
                fill_rat = pv_data['fill_rate']
                fill_rate = '%.2f%%' % (fill_rat * 1)
                # 广告位曝光率
                exposure_rat = pv_data['exposure_rate']
                exposure_rate = '%.2f%%' % (exposure_rat * 1)
                # 点击率
                click_rat = pv_data['click_rate']
                click_rate = '%.2f%%' % (click_rat * 1)
                # 广告填充率
                ad_fill_rat = pv_data['ad_fill_rate']
                ad_fill_rate = '%.2f%%' % (ad_fill_rat * 1)
                # 广告曝光率
                ad_exposure_rat = pv_data['ad_exposure_rate']
                ad_exposure_rate = '%.2f%%' % (ad_exposure_rat * 1)
                # 点击成本(元)
                cpc = pv_data['cpc']
                # 写入到CSV文件中
                csv_writer.writerow([f"{report_day}",f"{medium_name}",f"{media_id}",f"{placement_type}",f"{placement_name}",f"{placement_id}", f"{revenue}", f"{ecpm}", f"{request_count}", f"{return_count}", f"{ad_request_count}", f"{ad_return_count}", f"{pv}", f"{click}", f"{fill_rate}", f"{exposure_rate}", f"{click_rate}", f"{ad_fill_rate}", f"{ad_exposure_rate}", f"{cpc}"])
            return f"昨日{yesterday}有数据，已下载完成"

        else:
            return f"昨日{yesterday}数据为空"

# -----------------------------登录后台海量引擎广告投放后台管理系统--------------------------------------

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
def file_name(name):
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
    with open(ob_name, 'rb') as f1:
        # 请求参数
        files = [('file', f1)]
        # 发送请求
        reps = requests.post(api_url, files=files, headers=header)
        # 打印内容
        # assert reps.text[0:4] == "导入成功"
        if reps.text[0:4] == "导入成功":
            return reps.text
        else:
            return f"导入失败：{reps.text}"

def main():
    adnet_sso = ylh_login("1440186482", "hebeihailiang1234")
    # print(adnet_sso)
    if adnet_sso != None:
        yesterdayData = export_report(adnet_sso)
        print(yesterdayData)
        if yesterdayData == f"昨日{yesterday}数据为空":
            print("不进行导入")
            os.remove(file)
        else:
            print(file_name(ob_name))
            time.sleep(60)
            os.remove(ob_name)
    else:
        print("登录失败，关键信息未获取")

if __name__ == '__main__':
    main()
    # adnet_sso = ylh_login("1440186482", "hebeihailiang1234")
    # print(export_report(adnet_sso))
    # BlockingScheduler
    # scheduler = BlockingScheduler()
    # job = scheduler.add_job(main, 'cron', day_of_week='1-6', hour='*', minute=47)
    # scheduler.start()
    # job.remove()



