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
    while begin < end:
        mid = (begin + end) // 2
        if data_list[mid] < data_list[mid + 1]:
            begin = mid+1
        elif data_list[mid] < data_list[mid - 1]:
            end = mid-1
        else:
            result_index = mid
            break
    if begin == end:
        result_index = begin
    return result_index


def doubly_search(data, item):
    max = find_max(data)
    if max == -1:
        raise ValueError
    result = []
    if item > data[max] or (item < data[0] and item < data[-1]):
        return -1
    elif item == data[max]:
        result.append(max)
    else:
        if data[0] < item < data[max]:
            low = binary_search(data[:max], item)
            if low != -1:
                result.append(low)
        if data[-1] < item <= data[max]:
            high = binary_search(data[max:], item, reverse=True)
            if high != -1:
                result.append(high + max)

    if len(result) == 0:
        result.append(-1)

    return tuple(result)


if __name__ == '__main__':
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 7))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 3))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9, 6, 3, 2, 1, 0], 9))
    print(doubly_search([1, 3, 4, 6, 7, 8, 9], 9))

