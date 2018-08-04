#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 22:42
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.9.py
# @Software: PyCharm
from Chapter1_Fundamentals.counter import Counter
from common.time_utils import time_elapsed_deco


@time_elapsed_deco
def binary_search_recursion(search_list, search_item):
    """
    递归方式实现二分查找
    :param search_list:
    :param search_item:
    :return:
    """
    counter = Counter("search counter")
    result_index = search_impl(search_list, search_item, 0, len(search_list) - 1, depth=0, counter=counter)
    print(counter.counter)
    return result_index


def search_impl(search_list, search_item, start, end, depth, counter):
    print("{0} recursion {1}: start={2},end={3}".format(" " * depth, depth, start, end))
    depth += 1
    if start > end:
        return -1
    mid = (start + end) // 2
    guess = search_list[mid]
    counter.counter_inc()
    if guess > search_item:
        search_impl(search_list, search_item, start, mid - 1, depth, counter)
    elif guess < search_item:
        search_impl(search_list, search_item, mid + 1, end, depth, counter)
    else:
        return mid


if __name__ == '__main__':
    binary_search_recursion([x for x in range(100)], 23)
