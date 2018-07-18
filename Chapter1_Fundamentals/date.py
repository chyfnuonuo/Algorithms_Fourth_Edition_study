#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 21:46
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : date.py
# @Software: PyCharm


class Date(object):

    def __init__(self, year=1900, month=1, day=1):
        self.__month = month
        self.__year = year
        self.__day = day

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 0:
            raise ValueError("year must bigger than 0")
        self.__year = year

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if month < 1 or month > 12:
            raise ValueError("month must between 1 and 12")
        self.__month = month

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if day < 1 or day > 31:
            raise ValueError("month must between 1 and 31")

    def __str__(self):
        return "{0}/{1}/{2}".format(self.month, self.day, self.year)

    __repr__ = __str__


if __name__ == '__main__':
    date = Date(year=2017, month=12, day=24)
    print(date)
    date.month = 13
