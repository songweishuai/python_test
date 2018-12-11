# /usr/bin/python3
# -*- coding:utf-8 -*-
# 遍历目录文件

import os
import glob
import re

# for FileName in os.path.join("/opt/thunder/bin/dhcp", "STBs/*.ini"):
#     print("FileName:", FileName)

# print(os.path.join("/opt/thunder/bin/dhcp", "STBs/*.ini"))

# for FileName in glob.glob(os.path.join("/opt/thunder/bin/dhcp", "STBs/*ini")):
# for FileName in glob.glob("/opt/thunder/bin/dhcp/STBs/*.ini"):
#     print("FileName:", FileName)
#     head, tail = os.path.split(FileName)
#     print("head={0},tail={1}".format(head, tail))
#     root, exp = os.path.splitext(FileName)
#     print("root={0},exp={1}".format(root, exp))
#     input("\n\n按Enter键继续")


# for filename in glob.glob(os.path.join("/opt/thunder/bin/dhcp", "STBs/*.ini")):
# for filename in glob.glob("/opt/thunder/bin/dhcp/STBs/*.ini"):
#     head, tail = os.path.split(filename)
#     print("head:", head, "tail:", tail)
#
#     fname, _ = os.path.splitext(tail)
#     print("fname:", fname)

for FileName in glob.glob("/opt/thunder/bin/dhcp/STBs/*.ini"):
    print("FileName:", FileName)
    matchObj = re.match(r'/opt/thunder/bin/dhcp/STBs/(.*).ini', FileName, re.M | re.I)
    if matchObj:
        print("matchObj.group(1):", matchObj.groups())
    else:
        print("No Match")
    input("\n\n Please Click Enter Go on")
