#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 22:23
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.1.26.py
# @Software: PyCharm


def sort(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c


if __name__ == '__main__':
    print(sort(2, 1, 3))
