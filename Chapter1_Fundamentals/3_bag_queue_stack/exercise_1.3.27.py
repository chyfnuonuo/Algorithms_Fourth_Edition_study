#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 22:34
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.27.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


def max(first_node):
    result = 0
    while first_node.next_node is not None:
        if first_node.item_value > result:
            result = first_node.item_value
        first_node = first_node.next_node
    return result


if __name__ == '__main__':
    link_list= LinkList()
    link_list.append(Node(1))
    link_list.append(Node(2))
    link_list.append(Node(7))
    link_list.append(Node(3))
    link_list.append(Node(5))
    link_list.append(Node(11))
    link_list.append(Node(1))
    link_list.append(Node(3))
    link_list.append(Node(6))
    print(max(link_list[0]))

