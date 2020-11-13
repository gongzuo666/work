#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : ThreeReport.py
# Author: tian guang yuan
# Time  : 2020/11/9 10:24
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
from selenium.webdriver.common.action_chains import ActionChains
# 这两行是实现无界面的关键代码
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 实现静默模式，在电脑上不显示页面

# 取消浏览器出现'Chrome正在受到自动软件的控制'
# option=webdriver.ChromeOptions()
# option.add_experimental_option("excludeSwitches", ['enable-automation'])
#打开浏览器
driver=webdriver.Chrome()

def login(name,password):

    # 访问网址
    driver.get("https://sso.e.qq.com/login/hub?sso_redirect_uri=https%3A%2F%2Fe.qq.com%2Fdev%2Flogin%3F&service_tag=14")

    # 设置为全屏展示
    driver.maximize_window()
    # 刷新页面
    driver.refresh()
    # # 切换到这个内嵌网页
    eIframe = driver.find_element_by_css_selector("#qqLoginFrame")
    driver.switch_to.frame(eIframe)
    time.sleep(1)
    eleIframe = driver.find_element_by_css_selector("#ptlogin_iframe")
    driver.switch_to.frame(eleIframe)
    time.sleep(5)
    driver.find_element_by_css_selector("body >div > div#bottom_qlogin > #switcher_plogin").click()
    # driver.find_element_by_link_text("帐号密码登录").click()
    # 2 输入搜索关键词 python
    driver.find_element_by_css_selector(".inputstyle").send_keys(name)
    driver.find_element_by_css_selector(".inputstyle.password").send_keys(password)
    driver.find_element_by_css_selector(".btn").click()
    # # 等待
    time.sleep(5)
    print(driver.get_cookies()[-2]['value'])
    driver.close()
    # # 刷新页面
    # driver.refresh()
    # # 等待
    # time.sleep(5)
    # # 刷新页面
    # driver.refresh()
    # # 等待
    # time.sleep(5)
    # ele = driver.find_element_by_css_selector(".frame-sidebar > ul > li:nth-child(4)")
    # # 对定位到的元素执行鼠标悬停的操作
    # ActionChains(driver).move_to_element(ele).perform()
    # driver.find_element_by_css_selector(".frame-sidebar > ul > li:nth-child(4) >ul > li").click()
    # time.sleep(5)
    # # 全选广告位类型
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(3)").click()
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(3) .selection-drop > ul > li").click()
    # # 全选媒体
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(4)").click()
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(4) .selection-drop > ul > li").click()
    # time.sleep(1)
    # # 全选广告位
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(5)").click()
    # driver.find_element_by_css_selector(".frame-content .form-group > .size-160.module-selection:nth-child(5) .selection-drop > ul > li").click()
    #
    # # 日期昨天
    # driver.find_element_by_css_selector(".frame-content .form-group > .spa-ui").click()
    # driver.find_element_by_css_selector(".daterangepicker.dropdown-menu.show-calendar.opensright > div.ranges > ul > li").click()
    #
    # # 点击查询
    # driver.find_element_by_css_selector(".frame-content .form-group > a.btn").click()
    #
    # time.sleep(10)
    # driver.find_element_by_css_selector(".frame-content .form-group > .btn-wrapper").click()
    # print("点击了下载")
    # time.sleep(2)

if __name__ == '__main__':
    print(login("1440186482 ", "hebeihailiang123"))













