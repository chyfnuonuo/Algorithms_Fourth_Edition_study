#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 20:45
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : bag.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


class Bag(object):
    def __init__(self):
        self.__data_list = []

    def add(self, item):
        self.__data_list.append(item)

    def is_empty(self):
        return len(self.__data_list) == 0

    def __len__(self):
        return len(self.__data_list)


class BagUseLinkList(object):
    def __init__(self):
        self.__data_list = LinkList()

    def add(self, item):
        node = Node(item)
        self.__data_list.append(node)

    def is_empty(self):
        return self.__data_list.is_empty()

    def __len__(self):
        return len(self.__data_list)

    def __iter__(self):
        self.__data_list.__iter__()
        return self

    def __next__(self):
        return self.__data_list.__next__()


if __name__ == '__main__':
    bag = BagUseLinkList()
    bag.add(1)
    bag.add(3)
    bag.add(4)
    for node in bag:
        print(node)
