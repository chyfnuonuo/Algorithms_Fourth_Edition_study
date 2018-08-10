#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 22:08
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.15.py
# @Software: PyCharm


def two_sum_faster(data_list):
    temp_list = [None] * len(data_list)
    result = 0
    for data in data_list:
        if data < 0:
            temp_list[-data] = 1
        else:
            if temp_list[data] is not None:
                result += 1
    return result


if __name__ == '__main__':
    print(two_sum_faster([-8, -4, -2, 0, 1, 2, 4, 5, 8]))
