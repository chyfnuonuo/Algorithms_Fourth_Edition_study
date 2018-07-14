#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/5/6'
__contact__ = 'chengyoufu@gmail.com'
"""
from common.list_utils import get_random_list
from common.time_utils import time_elapsed_deco


@time_elapsed_deco
def shellsort(to_sort_list):
    lenth = len(to_sort_list)
    h = 1
    while h < lenth // 3:
        h = 3 * h + 1
    while h >= 1:
        index = h
        while index < lenth:
            jindex = index
            while jindex >= h and to_sort_list[jindex] < to_sort_list[jindex - h]:
                exch(to_sort_list, jindex, jindex - h)
                jindex -= h
            index += 1
        h = h // 3
    return to_sort_list


def exch(exc_list, srcindex, destindex):
    temp, exc_list[srcindex] = exc_list[srcindex], exc_list[destindex]
    exc_list[destindex] = temp


if __name__ == '__main__':
    src_list = get_random_list(start=0, end=1000000, lenth=10000)
    print(shellsort(src_list))
