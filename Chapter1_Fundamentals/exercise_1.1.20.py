#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 22:35
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.1.20.py
# @Software: PyCharm
from math import log


def ln(num):
    if num == 1:
        return 0
    else:
        return log(num)+ln(num-1)


if __name__ == '__main__':
    print(ln(10))

    
    