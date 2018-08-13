#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 22:40
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.4.10.py
# @Software: PyCharm

def binary_search(search_list, search_item):
    """
    二分查找
    :param search_list: 查找的有序列表
    :param search_item: 需要查找的项
    :return: 查找项所在的序列id
    """
    result_list = []
    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid = (start + end) // 2
        guess = search_list[mid]
        if guess > search_item:
            end = mid - 1
        elif guess < search_item:
            start = mid + 1
        else:
            result_list.append(mid)
            end = mid - 1
    if len(result_list) != 0:
        return result_list.pop()
    else:
        return -1


if __name__ == '__main__':
    s_list = [1, 3, 3, 3, 3, 5, 6, 7, 8, 9]
    print(binary_search(s_list, 3))
    s_list = [3, 3, 3, 3, 3, 5, 6, 7, 8, 9]
    print(binary_search(s_list, 3))
    s_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(binary_search(s_list, 3))
    s_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(binary_search(s_list, 1))
    s_list = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8]
    print(binary_search(s_list, 7))
