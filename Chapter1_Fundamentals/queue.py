#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 22:06
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : queue.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


class Queue(object):

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def __len__(self):
        return len(self.__list)


class QueueUseLink(object):
    def __init__(self):
        self.__list = LinkList()

    def enqueue(self, item):
        self.__list.append(Node(item))

    def dequeue(self):
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    pass
