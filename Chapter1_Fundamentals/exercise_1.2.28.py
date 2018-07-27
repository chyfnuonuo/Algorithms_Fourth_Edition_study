#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 22:48
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.28.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


def max(node):
    result = node.item_value
    if node.next_node is None:
        return result
    temp = max(node.next_node)
    if result > temp:
        return result
    else:
        return temp


if __name__ == '__main__':
    link_list = LinkList()
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
