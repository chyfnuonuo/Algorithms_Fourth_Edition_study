#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 22:17
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.39.py
# @Software: PyCharm
import random
import threading
import time

from Chapter1_Fundamentals.bagqueuestack.circle_list import CircleList
from Chapter1_Fundamentals.bagqueuestack.link_list import Node


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


class RingBufferTest(object):

    def __init__(self):
        self.__buffer = RingBuffer()

    def producer(self):
        print('process {} to write...'.format(threading.current_thread().getName()))
        for value in range(10):
            print('put {} to queue...'.format(value))
            self.__buffer.put(value, timeout=15)
            time.sleep(random.random() * 10)

    def consumer(self):
        print('process {} to read...'.format(threading.current_thread().getName()))
        while True:
            value = self.__buffer.get(timeout=15)
            print('get {} from queue...'.format(value))

    def run(self):
        pw = threading.Thread(target=self.consumer, name='consumer')
        pr = threading.Thread(target=self.producer, name='producer')
        pw.start()
        pr.start()
        pw.join()
        pr.join()


if __name__ == '__main__':
    test = RingBufferTest()
    test.run()
