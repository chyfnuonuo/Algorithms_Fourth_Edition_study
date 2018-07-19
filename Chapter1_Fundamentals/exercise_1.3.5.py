#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 23:14
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.5.py
# @Software: PyCharm
from basic.datastructure.link_list_demo import LinkList, Node


def convert_binary(num):
    """
    把十进制数字转换为二进制
    :param num: 需要转换的数字
    :return:
    """
    stack = LinkList()
    while num > 0:
        stack.push(Node(num % 2))
        num = num // 2
    result = 0
    for node in stack:
        result = result * 10 + node.item_value
    return result


if __name__ == '__main__':
    print(convert_binary(50))
    print(convert_binary(4))
    print(convert_binary(2))
