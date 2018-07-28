#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 23:29
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.29.py
# @Software: PyCharm
from Chapter1_Fundamentals.link_list import Node
from common.func_utils import type_check_deco


class CircleList(object):

    def __init__(self):
        self.__last_node = None

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

    def dequeue(self):
        if self.__last_node is not None:
            temp = self.__last_node.next_node
            if self.__last_node.next_node == self.__last_node:
                self.__last_node = None
            else:
                self.__last_node.next_node = self.__last_node.next_node.next_node

            return temp
        else:
            raise EOFError


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
