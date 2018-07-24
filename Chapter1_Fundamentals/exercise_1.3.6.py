#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 22:44
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.6.py
# @Software: PyCharm
from Chapter1_Fundamentals.queue import QueueUseLink
from Chapter1_Fundamentals.stack import Stack


def reverse(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())


if __name__ == '__main__':
    queue = QueueUseLink()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    reverse(queue)
    for item in queue:
        print(item)
