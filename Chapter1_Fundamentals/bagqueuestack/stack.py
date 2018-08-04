#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 6:54
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : stack.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.link_list import LinkList, Node


class Stack(object):
    def __init__(self):
        self.__list = LinkList()

    def push(self, item):
        self.__list.push(Node(item))

    def pop(self):
        return self.__list.pop().item_value

    def peek(self): # add exercise 1.3.7
        return self.__list[0].item_value

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
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
