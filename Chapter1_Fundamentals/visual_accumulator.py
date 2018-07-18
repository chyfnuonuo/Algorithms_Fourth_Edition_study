#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 22:07
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : accumulator.py
# @Software: PyCharm
import random

import matplotlib.pyplot as plt


class VisualAccumulator(object):

    def __init__(self):
        self.fig = plt.figure(figsize=(8, 4))
        self.__total = 0
        self.__data_num = 0
        self.data_list = []

    def show_fig(self):
        x = range(self.__data_num)
        plt.scatter(x, self.data_list)
        z = [sum(self.data_list) / self.__data_num] * self.__data_num
        plt.plot(x, z, label="$mean value$", color="red", linewidth=2)
        plt.show()

    def add_data(self, data):
        self.__total += data
        self.data_list.append(data)
        self.__data_num += 1
        self.show_fig()

    def cal_mean(self):
        return self.__total / self.__data_num

    def __str__(self):
        return "mean value of {0} numbers is {1}".format(self.__data_num, self.__total)


if __name__ == '__main__':
    accu = VisualAccumulator()
    for i in range(100):
        accu.add_data(random.randint(0, random.randint(50,100)))
    print(accu.cal_mean())
    print(accu)
