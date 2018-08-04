#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 21:41
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.30.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


def reverse(first_node):
    reverse_node = None
    while first_node is not None:
        second_node = first_node.next_node
        first_node.next_node = reverse_node
        reverse_node = first_node
        first_node = second_node
    return reverse_node


def reverse_use_recursion(first_node):
    if first_node is None or first_node.next_node is None:
        return first_node
    second_node = first_node.next_node
    reverse_node = reverse_use_recursion(second_node)
    second_node.next_node = first_node
    first_node.next_node = None
    return reverse_node


if __name__ == '__main__':
    link_list = LinkList()
    link_list.append(Node(1))
    link_list.append(Node(2))
    link_list.append(Node(3))
    link_list.append(Node(4))
    reverse = reverse_use_recursion(link_list[0])
    print(reverse)
