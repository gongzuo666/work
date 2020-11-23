#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 重试机制应用.py
# Author: tian guang yuan
# Time  : 2020/11/12 11:14
# -*-coding: gb2312 -*-
from selenium import webdriver
from retrying import retry

# 这两行是实现无界面的关键代码
option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 实现静默模式，在电脑上不显示页面
option.add_argument('window-size=1300,1300')  # 设置浏览器窗口大小
option.add_argument('--start-maximized')
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
    print(True)
    ele[0].send_keys('15100978670')
  else:
    print(False, len(ele))
    raise Exception("这不是我想要的数")
  driver.find_element_by_css_selector('[placeholder="请输入您的密码"]').send_keys('123456as')
  driver.find_element_by_css_selector('[type="button"]').click()
  driver.quit()

if __name__ == '__main__':
  randnum()





