#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : cc.py
# Author: tian guang yuan
# Time  : 2020/11/13 16:19

from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
def tick():
    # print('Tick! The time is: %s' % datetime.now())
    aa = '1231323'
    logging.basicConfig(level=logging.debug(aa),
                        format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    # 开始使用log功能
    logging.info('这是 loggging info message')
    logging.debug('这是 loggging debug message')

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
