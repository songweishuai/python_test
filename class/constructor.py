# /usr/bin/python3
# -*- coding:utf-8 -*-
# 如果子类需要调用父类的构造方法就需要显示的调用，或者子类不重写父类的构造方法


class Father(object):
    def __init__(self, name):
        self.name = name
        print("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name


class Son(Father):
    # 复写构造函数
    def __init__(self, name):
        print("hi")
        # 需要主动调用父类的构造方法
        # super().__init__(name)
        # Father.__init__(self, name)
        self.name = name

    def getName(self):
        return "son " + self.name


if __name__ == "__main__":
    son = Son('runoob')
    # print(son.getName())
    print(repr(son))
