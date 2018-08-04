#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 23:00
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : link_list_demo.py
# @Software: PyCharm
from copy import deepcopy

from common.func_utils import type_check_deco


class Node(object):

    def __init__(self, item_value, next_node=None):
        self.__item_value = item_value
        self.__next_node = next_node

    @property
    def item_value(self):
        return self.__item_value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError
        self.__next_node = next_node


class LinkList(object):
    def __init__(self):
        self.__first_node = None
        self.__last_node = None
        self.__length = 0
        self.__iter_node = self.__first_node
        self.__iter_modify_flag = False

    @property
    def first_node(self):
        return self.first_node

    @property
    def last_node(self):
        return self.last_node

    def is_empty(self):
        return self.__first_node is None

    @type_check_deco(object, Node)
    def append(self, new_node):
        """
        尾部追加
        :param new_node:
        :return:
        """
        if self.__first_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
        else:
            self.__last_node.next_node = new_node
            self.__last_node = new_node
        self.__iter_modify_flag = True
        self.__length += 1

    @type_check_deco(object, Node)
    def push(self, new_node):
        """
        头部追加
        :param new_node:
        :return:
        """
        new_node.next_node = self.__first_node
        self.__first_node = new_node
        if new_node.next_node is None:
            self.__last_node = new_node
        self.__iter_modify_flag = True
        self.__length += 1

    def pop(self):
        """
        弹出头部
        :return:
        """
        if self.__first_node is not None:
            temp = self.__first_node
            self.__first_node = self.__first_node.next_node
            temp.next_node = None
            self.__length -= 1
            if self.__first_node is None:
                self.__last_node = None
            self.__iter_modify_flag = True
            return temp
        else:
            raise EOFError

    @type_check_deco(object, int, Node)
    def insert(self, item_index, new_node):
        if item_index == self.__length - 1:
            self.append(new_node)
        elif item_index == 0:
            self.push(new_node)
        else:
            temp_node = self.__getitem__(item_index)
            temp_node.next_node, new_node.next_node = new_node, temp_node.next_node.next_node
            self.__length += 1
            self.__iter_modify_flag = True

    @type_check_deco(object, int)
    def remove(self, item_index):
        if item_index == 0:
            self.pop()
        else:
            temp_node = self.__getitem__(item_index - 1)
            if temp_node.next_node.next_node is None:
                temp_node.next_node = None
                self.__last_node = temp_node
            else:
                remove_node = temp_node.next_node
                temp_node.next_node = temp_node.next_node.next_node
                remove_node.next_node = None

            self.__length -= 1
            self.__iter_modify_flag = True

    def remove_after(self, item_index): # add exercise 1.3.24
        node = self.__getitem__(item_index)
        node.next_node = None
        self.__last_node = node
        self.__length = item_index + 1
        self.__iter_modify_flag = True

    def extend(self, other_link_list):  # exercise 1.3.47
        if not isinstance(other_link_list, LinkList):
            raise TypeError
        self.__last_node.next_node = other_link_list.__first_node
        self.__last_node = other_link_list.__last_node
        self.__iter_modify_flag = True

    def __iter__(self):
        self.__iter_node = self.__first_node
        self.__iter_modify_flag = False
        return self

    def reset_iter(self):
        self.__iter_node = self.__first_node
        self.__iter_modify_flag = False

    def __next__(self):
        if self.__iter_modify_flag:  # exercise 1.3.50
            raise Exception('List is modified in iterator')
        if self.__iter_node:
            temp_node = self.__iter_node
            self.__iter_node = self.__iter_node.next_node
            return temp_node
        else:
            raise StopIteration

    def __str__(self):
        return "Link list {1}".format(self.__doc__)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("other must be Node LinkList")
        result_list = deepcopy(self)
        result_list.extend(other)
        return result_list

    def __deepcopy__(self, memodict={}):
        new_link_list = self.__class__()
        for temp_node in self:
            new_link_list.append(deepcopy(temp_node, memodict))
        return new_link_list

    @type_check_deco(object, int)
    def __delitem__(self, item_index):  # exercise 1.3.20
        if item_index >= self.__length:
            raise IndexError("index {0} is out of range:[0:{1}]".format(item_index, self.__length - 1))
        result_node = self.__first_node
        for i in range(self.__length):
            if i == item_index - 1:
                break
            result_node = result_node.next_node
        result_node.next_node = result_node.next_node.next_node
        self.__length -= 1

    @type_check_deco(object, int, Node)
    def __setitem__(self, item_index, new_node):
        if item_index >= self.__length:
            item_index = self.__length
        result_node = self.__first_node
        for i in range(self.__length):
            if i == item_index:
                break
            result_node = result_node.next_node
        result_node.next_node, new_node.next_node = new_node.next_node, result_node.next_node

    @type_check_deco(object, int)
    def __getitem__(self, item_index):
        if item_index >= self.__length:
            raise IndexError
        result_node = self.__first_node
        for i in range(self.__length):
            if i == item_index:
                break
            result_node = result_node.next_node
        return result_node

    def __len__(self):
        return self.__length


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    link_list = LinkList()
    link_list2 = LinkList()
    # link_list2.append(1)
    link_list.append(node1)
    link_list.append(node2)
    link_list.append(node3)
    link_list.remove(2)
    # list_temp = link_list+link_list2
    # for node in list_temp:
    #     print(node.item_value)
    # for node in link_list:
    #     link_list.pop()
    #     link_list.pop()
    #     link_list.pop()
    #     print(node.item_value)
    # link_list.reset_iter()
    # for node in link_list:
    #     print(node.item_value)
