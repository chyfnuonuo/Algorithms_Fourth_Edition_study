#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 22:33
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.31.py
# @Software: PyCharm


class DoubleNode(object):

    def __init__(self, item):
        self.__item_value = item
        self.__pre_node = None
        self.__next_node = None

    @property
    def item_value(self):
        return self.item_value

    @property
    def pre_node(self):
        return self.pre_node

    @pre_node.setter
    def pre_node(self, other_node):
        if other_node is not None and not isinstance(other_node, DoubleNode):
            raise TypeError
        self.__pre_node = other_node

    @property
    def next_node(self):
        return self.pre_node

    @next_node.setter
    def next_node(self, other_node):
        if other_node is not None and not isinstance(other_node, DoubleNode):
            raise TypeError
        self.__next_node = other_node


class DoubleList(object):

    def __init__(self):
        self.__first_node = None
        self.__last_node = None
        self.__length = 0

    def is_empty(self):
        return self.__first_node is None

    def append(self,new_node):
        if self.__first_node is None:
            self.__first_node.next_node = new_node
            self.__last_node = new_node
        else:
            self.__last_node.next_node = new_node
            new_node.pre_node = self.__last_node
            self.__last_node = new_node
        self.__length+=1


    def push(self,new_node):
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            self.__first_node.pre_node = new_node
            new_node.next_node = self.__first_node
            self.__first_node = new_node
        self.__length+=1

    def pop(self):
        if self.__first_node is None:
            raise EOFError
        else:
            result = self.__first_node
            self.__first_node = self.__first_node.next_node
            self.__first_node.pre_node = None


    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass


    def __len__(self):
        return self.__length


if __name__ == '__main__':
    pass
