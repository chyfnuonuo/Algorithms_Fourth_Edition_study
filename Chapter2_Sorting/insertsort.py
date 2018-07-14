#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/5/6'
__contact__ = 'chengyoufu@gmail.com'
"""
from common.time_utils import time_elapsed_deco


@time_elapsed_deco
def insertsort1(to_sort_list):
    """
    插入排序
    :param to_sort_list:
    :return:
    """
    for i in range(len(to_sort_list)):
        key = to_sort_list[i]
        j = i - 1
        while j >= 0:
            if to_sort_list[j] > key:
                to_sort_list[j + 1], to_sort_list[j] = to_sort_list[j], key
            j = j - 1
    return to_sort_list


@time_elapsed_deco
def insertsort2(to_sort_list):
    """
    插入排序实现2，相比实现1减少了元素互换
    :param to_sort_list:
    :return:
    """
    for i in range(len(to_sort_list)):
        key = to_sort_list[i]
        j = i - 1
        while j >= 0 and to_sort_list[j] > key:
            to_sort_list[j + 1] = to_sort_list[j]
            j = j - 1
        to_sort_list[j + 1] = key
    return to_sort_list


if __name__ == '__main__':
    print(insertsort2([5, 3, 6, 1, 8, 7, 4]))
