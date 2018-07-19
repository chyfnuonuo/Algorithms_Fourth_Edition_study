#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 22:06
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : queue.py
# @Software: PyCharm


class Queue(object):

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def __len__(self):
        return len(self.__list)


if __name__ == '__main__':
    pass
