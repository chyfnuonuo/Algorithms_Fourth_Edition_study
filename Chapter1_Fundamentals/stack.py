#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 6:54
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : stack.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


class Stack(object):
    def __init__(self):
        self.__list = LinkList()

    def push(self, item):
        self.__list.push(Node(item))

    def pop(self):
        self.__list.pop().item_value

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def __iter__(self):
        self.__data_list.__iter__()
        return self

    def __next__(self):
        return self.__data_list.__next__()


if __name__ == '__main__':
    pass
