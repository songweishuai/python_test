#!/usr/bin/python3
# -*- conding:utf-8 -*-

import time
import pdb

# 获取时间戳
ticks = time.time()
print("当前时间戳:", ticks)

# 进入调试模式
pdb.set_trace()

# 获取当前时间
localTime = time.localtime()
print("本地时间：", localTime)

# 时间格式化
localTime = time.asctime(time.localtime(time.time()))
print("本地时间：", localTime)

import datetime

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
