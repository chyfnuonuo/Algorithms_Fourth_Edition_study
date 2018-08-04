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
        return self.__item_value

    @property
    def pre_node(self):
        return self.__pre_node

    @pre_node.setter
    def pre_node(self, other_node):
        if other_node is not None and not isinstance(other_node, DoubleNode):
            raise TypeError
        self.__pre_node = other_node

    @property
    def next_node(self):
        return self.__next_node

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

    @property
    def first_node(self):
        return self.__first_node

    @property
    def last_node(self):
        return self.__last_node

    def is_empty(self):
        return self.__first_node is None

    def append(self, new_node):
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            self.__last_node.next_node = new_node
            new_node.pre_node = self.__last_node
            self.__last_node = new_node
        self.__length += 1

    def push(self, new_node):
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            self.__first_node.pre_node = new_node
            new_node.next_node = self.__first_node
            self.__first_node = new_node
        self.__length += 1

    def pop(self):
        if self.__first_node is None:
            raise EOFError
        else:
            result = self.__first_node
            self.__first_node = self.__first_node.next_node
            if self.__first_node is not None:
                self.__first_node.pre_node = None
            else:
                self.__last_node = None
            result.next_node = None
        self.__length -= 1
        return result

    def insert(self, item_index, new_node):
        if item_index == 0:
            self.push(new_node)
        elif item_index == self.__length - 1:
            self.append(new_node)
        else:
            temp_node = self.__getitem__(item_index)
            temp_node.next_node = new_node
            new_node.next_node = temp_node.next_node.next_node
            new_node.pre_node = temp_node
            new_node.next_node.pre_node = new_node
        self.__length += 1

    def remove(self, item_index):
        if item_index == 0:
            self.pop()
        elif item_index == self.__length - 1:
            temp_node = self.__last_node.pre_node
            temp_node.next_node = None
            self.__last_node.pre_node = None
            self.__last_node = temp_node
            self.__length -= 1
        else:
            temp_node = self.__getitem__(item_index)
            temp_node.pre_node.next_node = temp_node.next_node
            temp_node.next_node.pre_node = temp_node.pre_node
            temp_node.next_node = None
            temp_node.pre_node = None
            self.__length -= 1

    def extend(self, other_list):
        self.__last_node.next_node = other_list.first_node
        other_list.first_node.pre_node = self.__last_node
        self.__last_node = other_list.last_node

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __getitem__(self, item_index):
        if item_index >= self.__length:
            raise EOFError
        result_node = self.__first_node
        for i in range(self.__length):
            if i == item_index:
                break
            result_node = result_node.next_node
        return result_node

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        return self.__length


if __name__ == '__main__':
    double_list = DoubleList()
    double_list.append(DoubleNode(1))
    double_list.append(DoubleNode(2))
    double_list.append(DoubleNode(3))
    double_list.append(DoubleNode(4))
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)
    double_list.push(DoubleNode(1))
    double_list.push(DoubleNode(2))
    double_list.push(DoubleNode(3))
    double_list.push(DoubleNode(4))
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)
    print(double_list.pop().item_value)