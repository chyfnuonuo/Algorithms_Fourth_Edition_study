#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 21:58
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : randomqueue_1.3.35.py
# @Software: PyCharm
import random


class RandomQueue(object):

    def __init__(self):
        self.__list = []

    def is_empty(self):
        return len(self.__list) == 0

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        item_index = random.randint(0, len(self.__list) - 1)
        self.__list[item_index], self.__list[len(self.__list) - 1] = self.__list[len(self.__list) - 1], self.__list[
            item_index]
        result = self.__list.pop(len(self.__list) - 1)
        return result

    def sample(self):
        item_index = random.randint(0, len(self.__list) - 1)
        return self.__list[item_index]


if __name__ == '__main__':
    pass
