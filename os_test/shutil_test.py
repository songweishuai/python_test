#!/usr/bin/python3
# -*- coding:utf-8 -*-

import shutil
import traceback

if __name__ == '__main__':
    archive = shutil.get_archive_formats()
    print("archive:", archive)

    # traceback.print_tb()

    # shutil.make_archive("/home/sws/test", "gztar", root_dir="/home/sws/demo/python/python_test/os_test",
    #                     base_dir="/home/sws/demo/python/python_test/")

    shutil.make_archive("/home/sws/test", "gztar", root_dir="/home/sws/demo/python/python_test/",
                        base_dir="./")
