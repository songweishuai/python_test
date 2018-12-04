#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试类使用


class JustCounter:
    # 私有属性
    __secret_count = 0
    publicCount = 0

    def count(self):
        self.__secret_count += 1
        self.publicCount += 1
        print(self.__secret_count)


def just_counter_test():
    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    try:
        print(counter.__secret_count)
    except:
        print("error catch")


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('我是{0},今年{1},体重{2}'.format(self.name, self.age, self.__weight))


class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # super(self, n, a, w)
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


def class_student_test():
    s = student('tim', 25, 120, 6)
    print('s:', s.name)


if __name__ == '__main__':
    print("main func begin")

    class_student_test()
