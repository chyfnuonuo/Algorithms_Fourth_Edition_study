#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 21:46
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : queuetest.py
# @Software: PyCharm
import random

from multiprocessing import Queue


class Printer(object):

    def __init__(self, page_rage):
        self.__page_rate = page_rage
        self.__current_task = None
        self.__time_remaining = 0

    def tick(self):
        if self.__current_task is not None:
            self.__time_remaining -= 1
            if self.__time_remaining <= 0:
                self.__current_task = None

    def is_busy(self):
        return self.__current_task is not None

    def start_task(self, new_task):
        self.__current_task = new_task
        self.__time_remaining = new_task.get_pages() * 60 / self.__page_rate


class Task(object):

    def __init__(self, current_second):
        self.__timestame = current_second
        self.__page_num = random.randint(1, 20)

    def get_pages(self):
        return self.__page_num

    def wait_time(self, current_time):
        return current_time - self.__timestame

class Processor(object):

    def __init__(self,second_num,pager_per_min):
        self.__queue = Queue()
        self.__printer= Printer(pager_per_min)
        self.__second_num=second_num

    def send_to_printer(self):


    def run(self):
        prodecer =

if __name__ == '__main__':
    queue =
