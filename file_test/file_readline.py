#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试file对象的readline函数使用

import sys

if __name__ == "__main__":
    # 使用try/except捕获错误
    try:
        file = open('./file.txt', mode='r')
    except OSError as err:
        print("Unexcepted error:", err)

    # file标识符(identitier)未定义
    # if not file:
    #     print("oper file error")

    # 使用with语句自动调用close函数
    # with open("file", mode="r") as file:
    #     re = file.readlines()
    #     print("文件内容:", re)
    # if not file:
    #     print("file closed")
    # else:
    #     print("文件名：", file.name)
    #     print("re:", re)
    #
    # print(type(re))

    # 写文件
    # writelines函数 参数为序列
    # write函数 参数为字符串
    # with open("file_out.txt", mode="w+") as file_out:
    #     file_out.writelines(re)

    file = open("./file", mode="r")
    print("文件名： ", file.name)
    re = file.readline(4)
    print("文件内容:", re)

    while True:
        re = file.readline()
        if not re:
            break
        print("文件内容：", re)
        # 使用file.tell返回文件当前位置
        p = file.tell()
        print("文件当前位置:", p)

    # 关闭文件
    file.close()
