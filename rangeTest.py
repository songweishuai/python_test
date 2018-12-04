#!/usr/bin/python3.6
# -*- coding:utf-8 -*-

for i in range(4):
    print(i)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in matrix:
#     print(row)

if __name__ == '__main__':
    print('main')
    list_1 = [[row[i] for row in matrix] for i in range(4)]
    print(list_1)
