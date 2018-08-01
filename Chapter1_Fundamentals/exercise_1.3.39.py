#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 22:17
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.39.py
# @Software: PyCharm
import os
import random
import threading
import time

from Chapter1_Fundamentals.circle_list import CircleList
from Chapter1_Fundamentals.link_list import Node


class RingBuffer(object):

    def __init__(self, buffer_length=-1):
        self.__buffer_length = buffer_length
        self.__data = CircleList()
        self.__lock = threading.Lock()
        self.__con = threading.Condition(self.__lock)

    def is_full(self):
        return len(self.__data) == self.__buffer_length

    def is_empty(self):
        return len(self.__data) == 0

    def put(self, item, timeout=None):
        if self.__con.acquire():
            while self.is_full():
                if not self.__con.wait(timeout):
                    raise TimeoutError
            self.__data.enqueue(Node(item))
            self.__con.notify()
            self.__con.release()

    def get(self, timeout=None):
        if self.__con.acquire():
            while self.is_empty():
                if not self.__con.wait(timeout):
                    raise TimeoutError
            result = self.__data.dequeue().item_value
            self.__con.notify()
            self.__con.release()
        return result


def write_queue(q):
    print('process {0} to write...'.format(os.getpid()))
    for value in range(10):
        print('put {0} to queue'.format(value))
        q.put(value, timeout=60)
        time.sleep(random.random())


def read_queue(q):
    print('process {0} to read...'.format(os.getpid()))
    while True:
        value = q.get(timeout=60)
        print('get {0} from queue'.format(value))


if __name__ == '__main__':
    que = RingBuffer()
    # pw = Process(target=write_queue,args=(que,))
    # pr = Process(target=read_queue,args=(que,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.join()
    # pr.terminate()
    write_queue(que)
    read_queue(que)
