#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 7:32
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : binary_search.py
# @Software: PyCharm
from common.time_utils import time_elapsed_deco


@time_elapsed_deco
def simple_search(search_list, search_item):
    """
    普通顺序查找实现方法
    :param search_list:
    :param search_item:
    :return:
    """
    for index, item in enumerate(search_list):
        if item == search_item:
            return index
    return None


@time_elapsed_deco
def binary_search(search_list, search_item):
    """
    二分查找
    :param search_list: 查找的有序列表
    :param search_item: 需要查找的项
    :return: 查找项所在的序列id
    """

    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid = (start + end) // 2
        guess = search_list[mid]
        if guess == search_item:
            return mid
        if guess < search_item:
            start = mid + 1
        else:
            end = mid - 1
    return None


if __name__ == '__main__':
    binary_search([x for x in range(100000)], 7)
    simple_search([x for x in range(100000)], 7)
    binary_search([x for x in range(100000)], 90000)
    simple_search([x for x in range(100000)], 90000)

    