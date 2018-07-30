#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 22:24
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.37.py
# @Software: PyCharm


def init_list(n):
    result_list = []
    for i in range(n):
        result_list.append(i)
    return result_list


def josephus(n, m):
    people_list = init_list(n)
    result_order = []
    while True:
        people_num = len(people_list)
        if people_num == 1:
            break
        else:
            pick_index = m % people_num
            result_order.append(people_list[pick_index])
            del people_list[pick_index]
    return result_order


if __name__ == '__main__':
    print(josephus(7, 10))
    print(josephus(10, 4))
