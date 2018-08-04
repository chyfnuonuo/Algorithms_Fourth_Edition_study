#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 22:07
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : accumulator.py
# @Software: PyCharm


class Accumulator(object):

    def __init__(self):
        self.__total = 0
        self.__data_num = 0

    def add_data(self, data):
        self.__total += data
        self.__data_num += 1

    def cal_mean(self):
        return self.__total / self.__data_num

    def __str__(self):
        return "mean value of {0} numbers is {1}".format(self.__data_num, self.__total)


if __name__ == '__main__':
    accu = Accumulator()
    accu.add_data(3)
    accu.add_data(4)
    accu.add_data(5)
    accu.add_data(6)
    print(accu.cal_mean())
    print(accu)
