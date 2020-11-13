#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 获取日期.py
# Author: tian guang yuan
# Time  : 2020/11/11 9:26
import datetime
# 今天的日期
today = datetime.date.today()
# 昨天的日期
yesterday = today - datetime.timedelta(days=6)
# 明天的日期
tomorrow = today + datetime.timedelta(days=1)

print(today, yesterday, tomorrow)













