#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 21:52
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.1.13.py
# @Software: PyCharm


def fibonacci(max_times):
    n, a, b = 0, 0, 1
    while n < max_times:
        yield a
        a, b = b, a + b
        n += 1


def get_fib(max_times):
    result_list = []
    for value in fibonacci(max_times):
        result_list.append(value)
    return result_list


if __name__ == '__main__':
    print(get_fib(100))
