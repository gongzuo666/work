#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 修改文件名.py
# Author: tian guang yuan
# Time  : 2020/11/18 16:59
import os

#查找文件
path="D:\\"
#os.listdir()方法，列出来所有文件
#返回path指定的文件夹包含的文件或文件夹的名字的列表
files=os.listdir(path)

#主逻辑
#对于批量的操作，使用FOR循环
for f in files:
    #调试代码的方法：关键地方打上print语句，判断这一步是不是执行成功
    print(f)
    if "tian" in f and f.endswith(".jpg"):
        print("原来的文件名字是:{}".format(f))

        #找到老的文件所在的位置
        old_file=os.path.join(path,f)
        print("old_file is {}".format(old_file))
        #指定新文件的位置，如果没有使用这个方法，则新文件名生成在本项目的目录中
        new_file=os.path.join(path,"优惠_2020-10-20.jpg")
        print("文件将更名为:{}".format(new_file))
        os.rename(old_file,new_file)
        print("修改后的文件名是:{}".format(new_file))






