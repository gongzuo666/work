#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 生成表格.py
# Author: tian guang yuan
# Time  : 2020/11/11 10:08
# 导入CSV安装包
import csv

# 1. 创建文件对象
f = open('./文件名.csv', 'w', encoding='utf-8')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 3. 构建列表头
csv_writer.writerow(["姓名","年龄","性别"])

# # 4. 写入csv文件内容
# csv_writer.writerow(["l",'18','男'])
# csv_writer.writerow(["c",'20','男'])
# csv_writer.writerow(["w",'22','女'])
#
# # 5. 关闭文件
# f.close()








