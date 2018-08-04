#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 22:47
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.10.py
# @Software: PyCharm
import random
import threading

import matplotlib.pyplot as plt


class VisualCounter(object):

    def __init__(self, counter_id, max_oper_times=0, max_value=10000):
        self.__counter_id = counter_id
        self.__counter = 0
        self.__lock = threading.Lock()
        self.__oper_times = 0
        self.__max_oper_times = max_oper_times
        self.__max_value = max_value
        self.__history_counter_list = []

    def reset_counter(self):
        self.__counter = 0
        self.__oper_times = 0
        self.__history_counter_list = []

    @property
    def counter(self):
        return self.__counter

    def counter_inc(self):
        if self.__counter == self.__max_value:
            raise ValueError("counter {0} is exceed limit {1}".format(self.__counter_id, self.__max_value))
        if self.__max_oper_times != 0 and self.__oper_times == self.__max_oper_times:
            raise ValueError("counter {0}'s operation times is exceed max limit:{1}".format(self.__counter_id,
                                                                                            self.__max_oper_times))
        with self.__lock:
            self.__counter += 1
            self.__oper_times += 1
            self.__history_counter_list.append(self.__counter)

    def counter_dec(self):
        if self.__counter == 0:
            raise ValueError("counter {0} is less than 0".format(self.__counter_id))
        if self.__max_oper_times != 0 and self.__oper_times == self.__max_oper_times:
            raise ValueError("counter {0}'s operation times is exceed max limit:{1}".format(self.__counter_id,
                                                                                            self.__max_oper_times))
        with self.__lock:
            self.__counter -= 1
            self.__oper_times += 1
            self.__history_counter_list.append(self.__counter)

    def show_fig(self):
        x = range(len(self.__history_counter_list))
        plt.plot(x, self.__history_counter_list, label="$counter value$", color="red", linewidth=2)
        plt.show()

    def __str__(self):
        return "Counter ID:{0}-->counter number is {1}".format(self.__counter_id, self.counter)

    __repr__ = __str__


if __name__ == '__main__':
    my_counter = VisualCounter("visual counter")
    for i in range(100):
        x = random.randint(0, 1)
        try:
            if x:
                my_counter.counter_inc()
            else:
                my_counter.counter_dec()

        except ValueError:
            pass

    my_counter.show_fig()
