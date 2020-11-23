#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 调试cokic登录.py
# Author: tian guang yuan
# Time  : 2020/11/12 9:57
import time
import json
import pprint
import requests
from selenium import webdriver
from retrying import retry
from 基础.loging模块 import FileLogger,ConsoleLogger

# 这两行是实现无界面的关键代码
option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 实现静默模式，在电脑上不显示页面
# option.add_argument('window-size=1300,1300')  # 设置浏览器窗口大小
# option.add_argument('--start-maximized')
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 不加载图片,加快访问速度
# option.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
# 访问网址
driver.get("http://110.249.209.202:46999/business/#/login")
# 设置为全屏展示
driver.maximize_window()

@retry(stop_max_attempt_number=3, wait_fixed=2000)
def randnum():

  # 用户名
  ele = driver.find_elements_by_css_selector('[placeholder="请输入您的手机号"]')
  if len(ele) > 0:
    print(True, len(ele))
    driver.find_element_by_css_selector('[placeholder="请输入您的手机号"]').send_keys('15100978670')
  else:
    print(False, len(ele))
    raise Exception("这不是我想要的数")
  driver.find_element_by_css_selector('[placeholder="请输入您的密码"]').send_keys('123456as')
  driver.find_element_by_css_selector('[type="button"]').click()
  time.sleep(5)
  return driver.get_cookies()[-2]['value']


def cokic():
    # 路径-url
    api_url = 'http://110.249.209.202:46999/merchant-product/web/product/show-list'
    header = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJiYzFmNTVmNCIsImlzcyI6IjI0ODkzMTRkNzI3Yjg5OWMiLCJqdGkiOiJoZ2xibzU2In0.kfB97JUJXN1aL4gtwTtKVmvavUS-YXioaRhR4mu4qMY",
        "content-type": "application/json;charset=UTF-8",
        "cookie": "tmId=1233223579320070146; tiId=1233223579215212546; isSetPayPassword=true; management-Token=f87b5ae1-8359-4862-863a-d6305d44a45d; sidebarStatus=width:%20230px; leftStatus=margin-left:%20230px%3B; translate=transform:translateX(0); Admin-Token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJiYzFmNTVmNCIsImlzcyI6IjI0ODkzMTRkNzI3Yjg5OWMiLCJqdGkiOiJvbmQwMDNjIn0.RyAsNyk1xxA_PJaGbzHDaRV2RK7b1VvVuyO4Jp4kECU; siId=1233223579261349889; phone=15100978670; trId=1233220943959175169; storeType=1; joinPhaseField=HOME; storeLogoUrl=http://110.249.209.202:46999/static/b/img/1233220943959175169/trader/20200228105055q2saapehehovmvz50l.jpg; storeName=%E7%94%B0%E6%B0%8F%E9%9D%92%E6%B5%B7%E8%A5%BF%E5%AE%81%E5%B8%82%E5%9F%8E%E4%B8%9C%E5%8C%BA; realName=%E7%94%B0%E5%85%89%E8%BF%9C; idCard=130531199012062658"}

    # 参数
    payload = json.dumps({
        "siId":"1233223579261349889","prodLocationStr":"","storeProdClassifyId":"","keyWords":"","pageSize":10,"pageNum":1
    })
    # sessions = requests.session()
    # requests.post('https://adnet.qq.com/report/getReportTableData', HTTP20Adapter())
    reps = requests.post(api_url, data=payload, headers=header)
    return reps.text

if __name__ == '__main__':
    log = FileLogger('songqin_vip_xt')
    # logi = ConsoleLogger()
    # print(randnum())
    # pprint.pprint(cokic())
    # driver.quit()
    log.info(cokic())
