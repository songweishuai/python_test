#!/usr/bin/python3
# -*- coding:utf-8 -*-

def test():
    def do_nonlocal():
        # nonlocal spam

        def do_nonlocal2():
            nonlocal spam
            spam = "nonlocal2 spam"

        do_nonlocal2()

    spam = "test spam"
    do_nonlocal()
    print("after nonlocal2 assigment:", spam)


if __name__ == "__main__":
    test()
