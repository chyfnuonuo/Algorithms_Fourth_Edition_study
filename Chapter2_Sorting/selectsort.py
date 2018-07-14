#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/5/5'
__contact__ = 'chengyoufu@gmail.com'
"""
from common.list_utils import get_random_list
from common.time_utils import time_elapsed_deco


def find_smallest(attr):
    """
    找出最小值
    :param attr:
    :return:
    """
    small_index = 0
    small_attr = attr[small_index]

    for itemIndex in range(len(attr)):
        if attr[itemIndex] < small_attr:
            small_attr = attr[itemIndex]
            small_index = itemIndex
    return small_index


@time_elapsed_deco
def select_sort1(sort_list):
    """
    选择排序方法1
    :param sort_list:
    :return:
    """
    new_list = []
    for i in range(len(sort_list)):
        small_index = find_smallest(sort_list)
        new_list.append(sort_list.pop(small_index))
    return new_list


@time_elapsed_deco
def select_sort2(sort_list):
    """
    选择排序方法2
    :param sort_list:
    :return:
    """
    for i in range(len(sort_list)):
        small_index = find_smallest(sort_list[i:])
        sort_list[i], sort_list[i + small_index] = sort_list[i:][small_index], sort_list[i]
    return sort_list


if __name__ == '__main__':
    src_list = get_random_list(start=0, end=1000000, lenth=10000)
    print(select_sort1(src_list))
    src_list = get_random_list(start=0, end=1000000, lenth=10000)
    select_sort2(src_list)
    print(src_list)
