#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 22:07
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.6.py
# @Software: PyCharm


def is_circular(str_a, str_b):
    if len(str_a) == len(str_b) and (str_a * 2).find(str_b) != -1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_circular("actgacg", "tgacgac"))
    print(is_circular("actwacg", "tgacgac"))
