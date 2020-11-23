#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Python重试机制.py
# Author: tian guang yuan
# Time  : 2020/11/13 16:19

import random
from retrying import retry

# 循环3次，间隔2秒
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def randnum():
    num = random.randint(0, 100)
    print(num)
    if num < 50:
        raise Exception("这不是我想要的数")

    return num


if __name__ == "__main__":
    num = randnum()
    print("success", num)
