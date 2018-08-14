#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 7:32
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : binary_search.py
# @Software: PyCharm
import random


from Chapter2_Sorting.quicksort import quick_sort
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
def binary_search(search_list, search_item,reverse=False):
    """
    二分查找
    :param search_list: 查找的有序列表
    :param search_item: 需要查找的项
    :return: 查找项所在的序列id
    """

    start = 0
    end = len(search_list) - 1
    if not reverse:
        while start <= end:
            mid = (start + end) // 2
            guess = search_list[mid]
            if guess > search_item:
                end = mid - 1
            elif guess < search_item:
                start = mid + 1
            else:
                return mid
    else:
        while start <= end:
            mid = (start + end) // 2
            guess = search_list[mid]
            if guess < search_item:
                end = mid - 1
            elif guess > search_item:
                start = mid + 1
            else:
                return mid
    return -1


@time_elapsed_deco
def binary_search_recursion(search_list, search_item):
    """
    递归方式实现二分查找
    :param search_list:
    :param search_item:
    :return:
    """
    return search_impl(search_list, search_item, 0, len(search_list) - 1)


def search_impl(search_list, search_item, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    guess = search_list[mid]
    if guess > search_item:
        search_impl(search_list, search_item, start, mid - 1)
    elif guess < search_item:
        search_impl(search_list, search_item, mid + 1, end)
    else:
        return mid


def random_test():
    binary_search([x for x in range(100000)], 7)
    simple_search([x for x in range(100000)], 7)
    binary_search_recursion([x for x in range(100000)], 7)
    binary_search([x for x in range(100000)], 90000)
    simple_search([x for x in range(100000)], 90000)
    for i in range(10):
        simple_search([x for x in range(100000)], random.randint(0, 100000))
        binary_search([x for x in range(100000)], random.randint(0, 100000))
        binary_search_recursion([x for x in range(100000)], random.randint(0, 100000))


def large_file_test():
    list_w = read_data("../data/largeW.txt")
    list_t = read_data("../data/largeT.txt")

    print('start sort')
    # quick_sort_use_stack(list_w, 0, len(list_w) - 1)
    quick_sort(list_w)
    # list_w.sort()
    result_list = []
    print('start search')
    for item in list_t:
        print('search {0} start'.format(item))
        result = binary_search(list_w, item)
        if result == -1:
            print('{0} not found'.format(item))
            result_list.append(item)
    write_to_file(result_list,"../data/result.txt")


def write_to_file(data,file):
    with open(file,'w') as f:
        for item in data:
            f.write(item)
            f.write("\n")


def read_data(file):
    result_list = []
    with open(file, 'r') as f:
        for line in f.readlines():
            result_list.append(line.strip())
    return result_list


if __name__ == '__main__':
    random_test()
    large_file_test()
