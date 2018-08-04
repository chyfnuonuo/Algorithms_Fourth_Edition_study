#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 23:08
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.26.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.link_list import LinkList, Node


def remove(link_list, key):
    temp_node = link_list[0]
    for node in link_list:
        if node.item_value == key:
            temp_node.next_node = node.next_node
        else:
            temp_node = node


if __name__ == '__main__':
    search_list = LinkList()
    search_list.append(Node(1))
    search_list.append(Node(2))
    search_list.append(Node(2))
    search_list.append(Node(3))
    search_list.append(Node(2))
    search_list.append(Node(4))
    remove(search_list, 2)
