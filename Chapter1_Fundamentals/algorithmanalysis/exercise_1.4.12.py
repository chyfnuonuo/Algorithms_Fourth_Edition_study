#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 22:49
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.12.py
# @Software: PyCharm


def find_common_data(first_list, second_list):
    first_index = 0
    second_index = 0
    first_length = len(first_list)
    second_length = len(second_list)
    result_list = []
    while first_index < first_length and second_index < second_length:
        if first_list[first_index] < second_list[second_index]:
            first_index += 1
        elif first_list[first_index] > second_list[second_index]:
            second_index += 1
        else:
            result_list.append(first_list[first_index])
            first_index += 1
            second_index += 1
    return result_list


if __name__ == '__main__':
    f_list = [1, 3, 5, 6, 7, 8, 9, 11, 12, 17]
    s_list = [3, 4, 6, 7, 9, 11, 13]
    print(find_common_data(f_list, s_list))
    f_list = [1, 3, 5, 6, 7, 8, 9, 11, 12, 17]
    s_list = [0, 2, 3, 4, 6, 7, 9, 11, 12, 13]
    print(find_common_data(f_list, s_list))
