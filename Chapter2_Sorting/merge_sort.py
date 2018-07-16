#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/5/13'
__contact__ = 'chengyoufu@gmail.com'
"""
from Chapter2_Sorting import insertsort
from common.list_utils import get_random_list
from common.time_utils import time_elapsed_deco


def merge_tow_sublist(first_sub_list, second_sub_list):
    """
    输入两个有序子序列进行归并排序,实现方法1
    :param first_sub_list:
    :param second_sub_list:
    :return:
    """
    temp_list = []
    first_list_index = 0
    first_list_lenth = len(first_sub_list)
    second_list_lenth = len(second_sub_list)
    second_list_index = 0
    for k in range(len(first_sub_list) + len(second_sub_list)):
        if first_list_index >= first_list_lenth:  # 左半部分的序列元素已经取尽,取右半部分下一个元素
            temp_list.append(second_sub_list[second_list_index])
            second_list_index += 1
        elif second_list_index >= second_list_lenth:  # 右半部分的序列元素已经取尽，取左半部分的下一个元素
            temp_list.append(first_sub_list[first_list_index])
            first_list_index += 1

        elif first_sub_list[first_list_index] >= second_sub_list[second_list_index]:  # 左右各取一个元素比较，取较小的元素
            temp_list.append(second_sub_list[second_list_index])
            second_list_index += 1
        else:
            temp_list.append(first_sub_list[first_list_index])
            first_list_index += 1
    return temp_list



def merge_tow_sublist_n(first_sub_list, second_sub_list):
    """
    输入两个有序子序列进行归并排序,实现方法2
    :param first_sub_list:
    :param second_sub_list:
    :return:
    """
    temp_list = []
    first_list_index = second_list_index = 0
    while second_list_index < len(first_sub_list) and first_list_index < len(second_sub_list):
        if first_sub_list[second_list_index] < second_sub_list[first_list_index]:
            temp_list.append(first_sub_list[second_list_index])
            second_list_index += 1
        else:
            temp_list.append(second_sub_list[first_list_index])
            first_list_index += 1

    if second_list_index == len(first_sub_list):
        for element in second_sub_list[first_list_index:]:
            temp_list.append(element)
    else:
        for element in first_sub_list[second_list_index:]:
            temp_list.append(element)

    return temp_list


def inner_list_merge(to_sort_list, lo, mid, hi):
    """
    对列表指定子序列原地归并排序
    :param to_sort_list: 需要排序的数组
    :param lo: 子序列起始索引
    :param mid: 子序列中间索引，左右都是有序数组
    :param hi: 子序列结尾索引
    :return:
    """
    left_list_index = lo
    right_list_index = mid + 1
    temp_list = to_sort_list[:]  # 使用临时变量保存列表内容
    k = lo
    while k < len(temp_list):
        if left_list_index > mid:  # 左半部分的序列元素已经取尽,取右半部分下一个元素
            to_sort_list[k] = temp_list[right_list_index]
            right_list_index += 1
        elif right_list_index > hi:  # 右半部分的序列元素已经取尽，取左半部分的下一个元素
            to_sort_list[k] = temp_list[left_list_index]
            left_list_index += 1

        elif temp_list[left_list_index] >= temp_list[right_list_index]:  # 左右各取一个元素比较，取较小的元素
            to_sort_list[k] = temp_list[right_list_index]
            right_list_index += 1
        else:
            to_sort_list[k] = temp_list[left_list_index]
            left_list_index += 1
        k += 1


@time_elapsed_deco
def merge_sort(to_sort_list):
    """
    普通归并排序
    :param to_sort_list:
    :return:
    """
    return merge_sort_impl(to_sort_list)


def merge_sort_impl(to_sort_list):
    if len(to_sort_list) <= 1:  # 不需要再拆分排序，直接返回
        return to_sort_list
    mid = len(to_sort_list) // 2
    left = merge_sort_impl(to_sort_list[:mid])  # 左半部分递归调用排序
    right = merge_sort_impl(to_sort_list[mid:])  # 右半部分递归调用排序
    return merge_tow_sublist(left, right)  # 将左右两个有序序列归并为一个有序序列


@time_elapsed_deco
def merge_sort_inner(to_sort_list):
    """
    原地归并排序，不用每次递归都产生一个新的列表
    :param to_sort_list:
    :return:
    """
    merge_sort_inner_impl(to_sort_list, 0, len(to_sort_list)-1)


def merge_sort_inner_impl(to_sort_list, lo, hi):
    """
    原地归并排序，不用每次递归都产生一个新的列表
    :param to_sort_list: 需要排序的列表
    :param lo: 需要排序的子列表起始元素序号
    :param hi: 需要排序的子列表终点元素序号
    :return:
    """
    if lo >= hi:  # 不需要再拆分排序，直接返回
        return
    mid = lo + (hi - lo) // 2
    merge_sort_inner_impl(to_sort_list, lo, mid)  # 左半部分递归调用原地排序
    merge_sort_inner_impl(to_sort_list, mid + 1, hi)  # 右半部分递归调用原地排序
    inner_list_merge(to_sort_list, lo, mid, hi)  # 将左右两个有序序列原地归并为一个有序序列


@time_elapsed_deco
def merge_sort_inner_with_insert(to_sort_list, lo, hi):
    """
    原地归并排序，不用每次递归都产生一个新的列表,数组长度小于4时使用插入排序
    :param to_sort_list: 需要排序的列表
    :param lo: 需要排序的子列表起始元素序号
    :param hi: 需要排序的子列表终点元素序号
    :return:
    """
    if hi - lo <= 4:  # 不需要再拆分排序，直接返回

        insertsort.insertsort2(to_sort_list[lo:hi])
        return
    mid = lo + (hi - lo) // 2
    merge_sort_inner_impl(to_sort_list, lo, mid)  # 左半部分递归调用原地排序
    merge_sort_inner_impl(to_sort_list, mid + 1, hi)  # 右半部分递归调用原地排序
    if to_sort_list[mid] <= to_sort_list[mid + 1]:  # 分别有序的子数组如果已经彼此有序，可以直接返回
        return
    inner_list_merge(to_sort_list, lo, mid, hi)  # 将左右两个有序序列原地归并为一个有序序列


@time_elapsed_deco
def merge_sort(to_sort_list):
    """
    自顶而下归并
    :param to_sort_list:
    :return:
    """
    inc_size = 1
    lenth = len(to_sort_list)
    while inc_size < lenth:
        lo = 0
        while lo + inc_size < lenth:
            if lo + inc_size + inc_size < lenth - 1:
                inner_list_merge(to_sort_list, lo, lo + inc_size - 1, lo + inc_size + inc_size)
            else:
                inner_list_merge(to_sort_list, lo, lo + inc_size - 1, lenth - 1)
            lo += inc_size + inc_size
        inc_size = inc_size + inc_size


if __name__ == '__main__': 0
# sort_list = [1, 3, 6, 7, 9, 2, 4, 7, 8, 10, 12]
# inner_list_merge(sort_list, 0, 4, 9)
# print(sort_list)
src_list = get_random_list(start=0, end=100000, lenth=1000000)
merge_sort(src_list)
print(src_list)
# subList1 = [1, 3, 6, 7, 9]
# subList2 = [2, 4, 7, 8, 10, 12]
# print(merge_tow_sublist(subList1, subList2))
# sort_list = [3, 5, 2, 4]
# merge_sort(sort_list)
# print(merge_sort(sort_list))
