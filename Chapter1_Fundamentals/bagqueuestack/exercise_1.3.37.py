#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 22:24
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.37.py
# @Software: PyCharm

from Chapter1_Fundamentals.bagqueuestack.myqueue import MyQueue


def init_queue(n):
    result_queue = MyQueue()
    for i in range(n):
        result_queue.enqueue(i)
    return result_queue


def josephus(n, m):
    people_queue = init_queue(n)
    result_order = []
    while len(people_queue) > 1:
        for i in range(m - 1):
            people_queue.enqueue(people_queue.dequeue())
        result_order.append(people_queue.dequeue())
    return result_order


if __name__ == '__main__':
    print(josephus(7, 3))
    print(josephus(10, 4))
