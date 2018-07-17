#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 7:02
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : counter.py
# @Software: PyCharm
import threading


class Counter(object):

    def __init__(self, counter_id, max_value=10000):
        self.__counter_id = counter_id
        self.__counter = 0
        self.__lock = threading.Lock()
        self.__max_value = max_value

    def reset_counter(self):
        self.__counter = 0

    @property
    def counter(self):
        return self.__counter

    def counter_inc(self):
        with self.__lock:
            self.__counter += 1
        if self.__counter > self.__max_value:
            raise ValueError("counter {0} is exceed limit {1}".format(self.counter, self.__max_value))

    def __str__(self):
        return "Counter ID:{0}-->counter number is {1}".format(self.__counter_id, self.counter)

    __repr__ = __str__


if __name__ == '__main__':
    pass
