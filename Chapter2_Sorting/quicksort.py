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


@time_elapsed_deco
def quick_sort(array, lo, hi):
    if lo < hi:
        q = partition1(array, lo, hi)
        quick_sort(array, lo, q - 1)
        quick_sort(array, q + 1, hi)


def partition(array, lo, hi):
    key = array[hi]
    i = lo - 1
    for j in range(lo, hi):
        if array[j] <= key:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[hi] = array[hi], array[i + 1]
    return i + 1


def partition1(par_list, lo, hi):
    key = par_list[lo]
    left_index = lo + 1
    right_index = hi
    while True:
        while par_list[left_index] < key:
            left_index += 1
            if left_index == hi:
                break
        while par_list[right_index] > key:
            right_index -= 1
        if left_index >= right_index:
            break
        par_list[left_index], par_list[right_index] = par_list[right_index], par_list[left_index]
    par_list[lo], par_list[right_index] = par_list[right_index], par_list[lo]
    return right_index


@time_elapsed_deco
def quick_sort_use_stack(array, lo, hi):
    if lo >= hi:
        return
    sort_stack = [lo, hi]
    # sort_stack.append(lo)
    # sort_stack.append(hi)
    while sort_stack:
        high = sort_stack.pop()
        low = sort_stack.pop()
        if high - low <= 0:
            continue
        key = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= key:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        sort_stack.extend([low, i, i + 2, high])


if __name__ == '__main__':
    src_list = get_random_list(start=0, end=1000000, lenth=10000)
    quick_sort(src_list, 0, 9999)
    print(src_list)
    src_list = get_random_list(start=0, end=1000000, lenth=10000)
    quick_sort_use_stack(src_list, 0, len(src_list) - 1)
    print(src_list)
