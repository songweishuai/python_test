#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试python异常处理

import sys


def test_1():
    # 测试ValueError
    while True:
        try:
            x = int(input("Please enter a number: "))
            print('*****')
            break
        except ValueError:
            print("Oops! That was no valid number. try again!")


def test_2():
    # 最后一个except子句没有异常类型
    try:
        f = open('myFile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print('OS error:{0}'.format(err))
    except ValueError:
        print('could not convert data to an interger')
    except:
        print('Unexpected error:', sys.exc_info())


def test_3():
    # try子句调用函数上抛异常
    try:
        raise NameError("XXXX")
    except NameError as err:
        print("An exception flew by!", err)
        raise


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as err:
        print('------:', err)
    else:
        print("result is {0}".format(result))
    finally:
        print('executing finally clause')


if __name__ == '__main__':
    print(sys.exc_info())
    print(sys.exec_prefix)

    test_1()

    test_2()

    try:
        test_3()
    except NameError as err:
        print("test_3 raise error is:", err)

    divide(2, 1)
    divide(2, 0)
    # divide('2', '1')
