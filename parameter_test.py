#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

if __name__ == '__main__':
    print(len(sys.argv))

    for n in range(len(sys.argv) - 1):
        print(sys.argv[n + 1])
        print('n:',n)
        # if n == (len(sys.argv) - 2):
        #   break
    else:
        print("use index")

    print("********************")

    for argv in sys.argv:
        print(argv)
