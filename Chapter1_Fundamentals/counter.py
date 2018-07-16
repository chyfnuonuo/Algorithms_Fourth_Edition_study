#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 7:02
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : counter.py
# @Software: PyCharm
import threading


class Counter(object):

    def __init__(self, counter=0, max_value=10000):
        self.__counter = counter
        self.__lock = threading.Lock()
        self.__max_value = max_value

    def reset_counter(self, counter=0):
        self.__counter = counter

    @property
    def counter(self):
        return self.__counter

    def counter_inc(self):
        with self.__lock:
            self.__counter += 1
        if self.__counter > self.__max_value:
            raise ValueError("counter {0} is exceed limit {1}".format(self.counter,self.__max_value))


if __name__ == '__main__':
    pass
