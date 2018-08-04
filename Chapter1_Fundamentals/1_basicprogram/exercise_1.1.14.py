#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 22:27
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.1.14.py
# @Software: PyCharm


def lg(value):
    num = 1
    temp = 2
    while temp <= value:
        temp = temp << 1
        num += 1
    return num - 1


if __name__ == '__main__':
    assert lg(3) == 1
    assert lg(8) == 3
    assert lg(9) == 3
    assert lg(15) == 3
    assert lg(16) == 4
