#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 21:26
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1_1_9.py
# @Software: PyCharm


def convert_to_binary(num):
    s = ""
    while num > 0:
        s = str(num % 2)+s
        num = num // 2
    return s


if __name__ == '__main__':
    print(convert_to_binary(4))
    print(convert_to_binary(5))
    print(convert_to_binary(1024))
