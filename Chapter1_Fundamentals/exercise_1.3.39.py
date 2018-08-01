#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 22:17
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.39.py
# @Software: PyCharm
import threading

from Chapter1_Fundamentals.circle_list import CircleList
from Chapter1_Fundamentals.link_list import Node


class RingBuffer(object):

    def __init__(self, buffer_length=100):
        self.__buffer_length = buffer_length
        self.__data = CircleList()
        self.__lock = threading.Lock()
        self.__con = threading.Condition(self.__lock)

    def is_full(self):
        return len(self.__data) == self.__buffer_length

    def is_empty(self):
        return len(self.__data == 0)

    def enqueue(self, item, timeout=None):
        if self.__con.acquire():
            while self.is_full():
                self.__con.wait(timeout)
            self.__data.enqueue(Node(item))
            self.__con.notify()
            self.__con.release()

    def dequeue(self):
        if self.__con.acquire():
            while self.is_empty():
                self.__con.wait()
            result = self.__data.dequeue().item_value
            self.__con.notify()
            self.__con.release()
        return result


if __name__ == '__main__':
    pass
