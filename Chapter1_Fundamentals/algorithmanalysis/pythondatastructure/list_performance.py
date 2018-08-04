#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 21:28
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : list_performance.py
# @Software: PyCharm
from timeit import Timer
import matplotlib.pyplot as plt

def test1():
    list_data = []
    for i in range(1000):
        list_data = list_data + [i]


def test2():
    list_data = []
    for i in range(1000):
        list_data.append(i)


def test3():
    list_data = [i for i in range(1000)]


def test4():
    list_data = list(range(1000))


def show_fig(self):
    x = range(self.__data_num)
    plt.scatter(x, self.data_list)
    z = [sum(self.data_list) / self.__data_num] * self.__data_num
    plt.plot(x, z, label="$mean value$", color="red", linewidth=2)
    plt.show()


if __name__ == '__main__':
    t1 = Timer('test1()', 'from __main__ import test1')
    t2 = Timer('test2()', 'from __main__ import test2')
    t3 = Timer('test3()', 'from __main__ import test3')
    t4 = Timer('test4()', 'from __main__ import test4')
    print('contact', t1.timeit(number=1000), 'ms')
    print('append', t2.timeit(number=1000), 'ms')
    print('comprehension', t3.timeit(number=1000), 'ms')
    print('list range', t4.timeit(number=1000), 'ms')

    list_data = list(range(10000000))
    pop_zero = Timer('list_data.pop(0)', 'from __main__ import list_data')
    pop_end = Timer('list_data.pop()', 'from __main__ import list_data')
    print('pop zero',pop_zero.timeit(number=1000),'ms')
    print('pop', pop_end.timeit(number=1000), 'ms')

    pop_zero = Timer('list_data.pop(0)', 'from __main__ import list_data')
    pop_end = Timer('list_data.pop()', 'from __main__ import list_data')
    for i in range(1000000, 100000001, 1000000):
        list_data = list(range(i))
        pt = pop_end.timeit(number=1000)
        list_data = list(range(i))
        pz = pop_zero.timeit(number=1000)
        print("%15.5f,	%15.5f" % (pz, pt))
