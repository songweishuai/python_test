#!/usr/bin/python3

import time

if __name__ == '__main__':
    time_stamp = "1556073415"
    print(time_stamp.isdigit())
    today = time.strftime("%Y-%m-%d", time.localtime())
    print(today)
    print(time.localtime())

    """
        时间戳按格式转换
    """
    last_day = time.strftime("%Y-%m-%d", time.localtime(int(time_stamp)))
    print(last_day)
    test = ("test", [("name", 6), ("sex", "man"), ("age", 8)])
