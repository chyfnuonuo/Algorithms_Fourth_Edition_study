#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/5/12'
__contact__ = 'chengyoufu@gmail.com'
"""
from Chapter1_Fundamentals import binary_search


def sum2count(oper_list):
    count = 0
    for index in range(len(oper_list)):
        if binary_search.binary_search(oper_list[index + 1:], -oper_list[index]) is not None:
            count += 1
    return count


print(sum2count([-8, -4, -2, 0, 1, 2, 4, 5, 8]))


def sum3count(oper_list):
    count = 0
    for i in range(len(oper_list)):
        for j in range(len(oper_list[i + 1:])):
            if binary_search.binary_search(oper_list[i + 1:][j + 1:], -(oper_list[i] + oper_list[i + 1:][j])) is not None:
                count += 1
    return count


print(sum3count([-3, -2, -1, 0, 1, 2, 3]))
