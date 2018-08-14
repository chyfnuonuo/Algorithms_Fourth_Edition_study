#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:59
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.16.py
# @Software: PyCharm

def closein_pair(data_list):
    data_list.sort()
    result = 0
    temp = data_list[1] - data_list[0]
    for index in range(len(data_list)-1):
        if data_list[index + 1] - data_list[index] < temp:
            temp = data_list[index + 1] - data_list[index]
            result = index
    return result, result + 1


if __name__ == '__main__':
    print(closein_pair([1.1, 2.2, 0.1, -1.7, 0.9, 2.3, 2.4]))
