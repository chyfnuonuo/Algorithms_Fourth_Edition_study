#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 23:28
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : randombag_1.3.34.py
# @Software: PyCharm
import random


class RandomBag(object):

    def __init__(self):
        self.__list = []

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def add(self, item):
        self.__list.append(item)

    def __iter__(self):
        random.shuffle(self.__list)
        self.__iter_start=0
        return self

    def __next__(self):
        if self.__iter_start==self.size():
            raise StopIteration
        result = self.__list[self.__iter_start]
        self.__iter_start+=1
        return result


if __name__ == '__main__':
    bag = RandomBag()
    bag.add(1)
    bag.add(2)
    bag.add(3)
    bag.add(4)
    bag.add(5)
    bag.add(6)
    for item in bag:
        print(item)
    for item in bag:
        print(item)
