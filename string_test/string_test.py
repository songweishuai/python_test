#!/usr/bin/python3
# -*- coding:utf-8 -*-

URLS = [
    (r'.*',
     (r'/', 'handler.index.indexHandler'),
     (r'/tasks/?(list|confirm)?', 'handler.index.tasksHandler')
     )
]

if __name__ == '__main__':
    # str = "我叫 %s 今年 %d 岁" % ("宋伟帅", 18)
    # str1 = "我叫 {name} 今年 {age} 岁".format(name="songweishuai", age=18)
    # print(str)
    # print(str1)
    #
    # a = bytes("a", "utf-8")
    # print(a)
    # b=a.decode()

    for spec in URLS:
        print(spec)
        for item in spec:
            print(item)

        # print(spec[1:])
