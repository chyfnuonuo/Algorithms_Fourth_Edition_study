#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 21:58
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : randomqueue_1.3.35.py
# @Software: PyCharm
import copy
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

    def __iter__(self):
        self.__start_index = 0
        self.__iter_list = copy.deepcopy(self.__list)
        random.shuffle(self.__iter_list)
        return self

    def __next__(self):
        if self.__start_index == len(self.__iter_list):
            raise StopIteration
        result = self.__iter_list[self.__start_index]
        self.__start_index += 1
        return result


if __name__ == '__main__':
    random_list = RandomQueue()
    random_list.enqueue(1)
    random_list.enqueue(2)
    random_list.enqueue(3)
    random_list.enqueue(4)
    random_list.enqueue(5)
    random_list.enqueue(6)
    for i in random_list:
        print(i)
    for i in random_list:
        print(i)


