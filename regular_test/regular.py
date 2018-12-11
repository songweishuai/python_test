#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试正则表达式

import re

line = "Cats are smarter than dogs"

# searchObj = re.search(r"(.*) are (.*?) .*", line, re.I | re.M)
# searchObj = re.search(r"(.*) are (.*?) .*", line, re.I | re.M)
pattern = re.compile(r"(.*) are (.*?) .*", re.I | re.M)
searchObj = re.search(pattern, line)
if searchObj:
    print("searchObj.group():", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing Found")

print(re.search("shuai", "songweishuai", re.I | re.M).start())
print(re.search("shuai", "songweishuai", re.I | re.M).span())

phone = "2004-959-559 # 这是一个号码"
# 删除注释
num = re.sub(r" .*$", "", phone)
print("num:", num)
# 移除非数字内容
num = re.sub(r"\D", "", phone)
print("num:", num)
