#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 21:43
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.20.py
# @Software: PyCharm
from Chapter1_Fundamentals.basicprogram.binary_search import binary_search


def find_max(data_list):
    begin = 0
    end = len(data_list) - 1
    result_index = -1
    while begin <= end:
        mid = (begin + end) // 2
        if data_list[mid] < data_list[mid + 1]:
            begin = mid
        elif data_list[mid] < data_list[mid - 1]:
            end = mid
        else:
            result_index = mid
            break
    return result_index


def doubly_search(data_list, search_item):
    max_index = find_max(data_list)
    if max_index == -1:
        raise ValueError
    result_list = []
    if search_item > data_list[max_index] or (search_item < data_list[0] and search_item < data_list[-1]):
        return -1

    if data_list[0] < search_item < data_list[max_index]:
        low_result = binary_search(data_list[:max_index], search_item)
        if low_result != -1:
            result_list.append(low_result)
    if data_list[-1] < search_item <= data_list[max_index]:
        high_result = binary_search(data_list[max_index:], search_item, reverse=True)
        if high_result != -1:
            result_list.append(high_result + max_index)
    if len(result_list) == 0:
        result_list.append(-1)

    return tuple(result_list)


if __name__ == '__main__':
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 7))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 3))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 9))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9], 9))
