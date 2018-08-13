#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:52
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.17.py
# @Software: PyCharm


def faraway_pair(data_list):
    min = data_list[0]
    max = data_list[0]
    min_index = 0
    max_index = 0
    for index, data in enumerate(data_list):
        if data < min:
            min = data
            min_index = index
        elif data > max:
            max = data
            max_index = index

    return min_index, max_index


if __name__ == '__main__':
    print(faraway_pair([0.1, -2.3, 4.5, 1.2, 6.1, -1.1]))
