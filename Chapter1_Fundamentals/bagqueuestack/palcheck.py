#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 22:15
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : palcheck.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.deque import Deque


def pal_check(string):
    dqueue = Deque()
    for ch in string:
        dqueue.push_right(ch)
    result = True
    while dqueue.size() > 1:
        left = dqueue.pop_left()
        right = dqueue.pop_right()
        if left != right:
            result = False
            break
    return result


if __name__ == '__main__':
    print(pal_check('qwerewq'))
    print(pal_check('qwereqq'))
