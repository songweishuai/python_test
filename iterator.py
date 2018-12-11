#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 迭代器使用


def iterator_test():
    a = [1, 2, 3, 4]
    i = iter(a)
    while True:
        try:
            print(next(i))
        except StopIteration:
            print("iterator_test end")
            break

    i = iter(a)
    for x in i:
        print(x)


class MyNumbers:
    def __iter__(self):
        print("__iter__")
        self.a = 1
        return self

    def __next__(self):
        print("__next__")
        x = self.a
        self.a += 1
        return x


def MyNumbersTest():
    myclass = MyNumbers()
    print()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))


if __name__ == '__main__':
    # iterator_test()

    MyNumbersTest()
