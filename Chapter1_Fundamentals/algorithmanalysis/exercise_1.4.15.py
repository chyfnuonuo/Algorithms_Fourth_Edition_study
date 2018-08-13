#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 22:08
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.15.py
# @Software: PyCharm


def two_sum_faster(data_list):
    begin = 0
    end = len(data_list) - 1
    result = 0
    while begin < end:
        if data_list[begin] + data_list[end] < 0:
            begin += 1
        elif data_list[begin] + data_list[end] > 0:
            end -= 1
        else:
            begin += 1
            end -= 1
            result += 1
    return result


# def three_sum_faster(data_list):
#     temp_list = [None] * len(data_list)
#     result = 0
#     for index1 in data_list；
#         for index2 in data_list[index1:]:
#             if data_list[index1]+data_list[index2]<0:
#                 temp_list[]


if __name__ == '__main__':
    print(two_sum_faster([-8, -4, -2, 0, 1, 2, 2, 4, 5, 8]))
