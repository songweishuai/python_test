#!/usr/bin/python3.6
# -*- coding:utf-8 -*-


def list_test():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(basket):
        print(f)

    print("**********************")

    # 反向遍历序列
    for i in reversed(basket):
        print(i)


def list_zip_test():
    # 使用zip函数遍历多个序列
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('what is your {0}? It is {1}'.format(q, a))


def dict_items_test():
    # test_dict = dict()
    # test_dict["hello"] = "world"
    # print(test_dict)
    ret = dict(code=1, count=0, msg='OK')
    print(ret)
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, val in knights.items():
        print(key, val)


def list_expression_test():
    vec = [2, 4, 6]
    list_1 = [3 * x for x in vec if x > 3]
    print(list_1)


if __name__ == '__main__':
    print('***main*****')
    list_test()

    # zip
    list_zip_test()

    # dict items
    dict_items_test()

    # list_expression
    list_expression_test()
