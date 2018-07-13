#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 22:43
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : list_utils.py
# @Software: PyCharm
import random


def get_random_list(start=0, end=9, lenth=10):
    """
    返回一个指定长度，指定随机数范围的整数随机数列表
    :param start:随机数起始值，默认为0
    :param end:随机数结束值，默认为9
    :param lenth:随机列表长度，默认为10
    :return:返回随机数列表
    """
    if not (isinstance(start, int) and isinstance(end, int) and isinstance(lenth, int)):
        raise TypeError
    if start > end or lenth < 0:
        raise ValueError
    random_list = []
    for x in range(lenth):
        random_list.append(random.randint(start, end))
    return random_list


if __name__ == '__main__':
    print(get_random_list())
    print(get_random_list())
