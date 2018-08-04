#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 23:15
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : Deque_1.3.33.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import LinkList, Node


class Deque(object):

    def __init__(self):
        self.__link_list = LinkList()

    def is_empty(self):
        return len(self.__link_list) == 0

    def size(self):
        return len(self.__link_list)

    def push_left(self, item):
        self.__link_list.push(Node(item))

    def push_right(self, item):
        self.__link_list.append(Node(item))

    def pop_left(self):
        return self.__link_list.pop().item_value

    def pop_right(self):
        result = self.__link_list[self.size() - 1]
        self.__link_list.remove(self.size() - 1)
        return result.item_value


if __name__ == '__main__':
    deque = Deque()
    deque.push_left(1)
    deque.push_left(2)
    deque.push_left(3)
    deque.push_right(3)
    deque.push_right(2)
    deque.push_right(1)
    print(deque.pop_left())
    print(deque.pop_left())
    print(deque.pop_left())
    print(deque.pop_right())
    print(deque.pop_right())
    print(deque.pop_right())
