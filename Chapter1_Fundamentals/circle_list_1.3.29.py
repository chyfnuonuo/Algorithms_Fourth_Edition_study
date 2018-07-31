#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 23:29
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : circle_list_1.3.29.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import Node
from common.func_utils import type_check_deco


class CircleList(object):

    def __init__(self):
        self.__last_node = None
        self.__iter_node = self.__last_node
        self.__length = 0

    def is_empty(self):
        return self.__last_node is None

    @type_check_deco(object, Node)
    def enqueue(self, node):
        if self.__last_node is None:
            self.__last_node = node
            self.__last_node.next_node = node
        else:
            node.next_node = self.__last_node.next_node
            self.__last_node.next_node = node
            self.__last_node = node
        self.__length+=1

    def dequeue(self):
        if self.__last_node is not None:
            temp = self.__last_node.next_node
            if self.__last_node.next_node == self.__last_node:
                self.__last_node = None
            else:
                self.__last_node.next_node = self.__last_node.next_node.next_node
            self.__length-=1
            return temp
        else:
            raise EOFError

    def __iter__(self):
        if self.__last_node is None:
            raise EOFError
        self.__iter_node = self.__last_node.next_node
        return self

    def __next__(self):

        if self.__iter_node is None:
            raise StopIteration
        elif self.__iter_node != self.__last_node:
            result = self.__iter_node
            self.__iter_node = self.__iter_node.next_node

        else:
            result = self.__iter_node
            self.__iter_node = None
        return result

    def __len__(self):
        return self.__length


if __name__ == '__main__':
    circle_list = CircleList()
    circle_list.enqueue(Node(1))
    circle_list.enqueue(Node(2))
    circle_list.enqueue(Node(3))
    circle_list.enqueue(Node(4))
    print(circle_list.dequeue().item_value)
    print(circle_list.dequeue().item_value)
    print(circle_list.dequeue().item_value)
    print(circle_list.dequeue().item_value)
    for item_node in circle_list:
        print(item_node.item_value)
    for item_node in circle_list:
        print(item_node.item_value)