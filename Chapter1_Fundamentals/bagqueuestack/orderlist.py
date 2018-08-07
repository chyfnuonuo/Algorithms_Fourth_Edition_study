#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 22:33
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : orderlist.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.link_list import Node


class OrderList(object):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add(self, item):
        new_node = Node(item)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            current = self.__head
            previous = None
            while current is not None:
                if item > current.item_value:
                    previous = current
                    current = current.next_node
                else:
                    break
            if previous is None:
                new_node.next_node = current
                self.__head = new_node
            else:
                previous.next_node = new_node
                new_node.next_node = current
        self.__length += 1

    def pop(self):
        if self.__head is not None:
            result_node = self.__head
            self.__head = result_node.next_node
            result_node.next_node = None
            self.__length -= 1
            return result_node.item_value
        else:
            raise EOFError




    def __len__(self):
        return self.__length


if __name__ == '__main__':
    pass
