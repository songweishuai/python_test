#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试python函数

sum = lambda arg1, arg2: arg1 + arg2
anonymous = lambda: '厉害'

o_count = 1


def outter():
    # 局部变量
    o_count = 1111

    # 闭包函数
    def inner_0():
        o_count = 222

        def inner():
            # 闭包函数内变量不可以在闭包函数调用
            i_count = 2
            # 变量的查找顺序 local->EnClosing->Global->Built-In
            # o_count在inner()函数是局部变量
            # o_count = 2
            # global o_count
            nonlocal o_count
            print('global o_count:', o_count)
            o_count = 22
            print('inner fun print o_count', o_count)

        inner()
        print('inner_0:',o_count)
    inner_0()


if __name__ == '__main__':
    print('相加后的值：', sum(10, 20))
    print('相加后的值:', sum(20, 40))

    # 没有参数的匿名函数
    print('无参数的匿名函数:', anonymous())

    # print('局部变量:', o_count)
    # print('闭包函数标量:',i_count)
    # o_count = 2
    # if o_count:
    # if语句不会引入新的作用域，在if语句代码块外也可以使用
    if_count = 3
    print('if_count:', if_count)

    outter()
