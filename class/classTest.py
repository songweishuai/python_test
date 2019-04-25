#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 测试类使用
# 支持继承，同时页支持多继承，classname(baseclassname1,baseclassname2,...)
# 调用子类未实现的方法，会按圆括号内基类的顺序从左向右查询
# 基类的私有方法不能2继承


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


class People:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('我是{0},今年{1},体重{2}'.format(self.name, self.age, self.__weight))

    def proud(self):
        print("I am an people")


class Boy:
    def speak(self):
        print("I am a boy")

    def __speak(self):
        print("I am a shuai")

    def proud(self):
        self.__speak()


class Girl:
    def speak(self):
        print("I am a Girl")


class Student(People, Boy, Girl):
    grade = ''

    def __init__(self, n, a, w, g):
        super().__init__(n, a, w)
        # People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        super().speak()
        Girl.speak(self)
        # People.speak(self)
        # Boy.speak(self)
        # G irl.speak(self)
        print("%s 说：我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


def class_student_test():
    s = Student('tim', 25, 120, 6)
    print('s:', s.name)
    s.speak()

    # 私有方法不能继承
    # s.__speak();
    s.proud()

    # 使用super方法调用父类的方法
    super(Student, s).proud()


if __name__ == '__main__':
    print("main func begin")

    class_student_test()
