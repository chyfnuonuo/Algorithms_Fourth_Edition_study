#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 21:46
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : date.py
# @Software: PyCharm


class Date(object):

    def __init__(self, year=1900, month=1, day=1):
        self.__year = year
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if 0 < day <= 31:
                self.__month = month
                self.__day = day
            else:
                raise ValueError("day value error")
        elif month in [4, 6, 9, 11]:
            if 0 < day <= 30:
                self.__month = month
                self.__day = day
            else:
                raise ValueError("day value error")
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if 0 < day <= 29:
                    self.__month = month
                    self.__day = day
                else:
                    raise ValueError("day value error")
            else:
                if 0 < day <= 28:
                    self.__month = month
                    self.__day = day
                else:
                    raise ValueError("day value error")
        else:
            raise ValueError("month value error")

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def __str__(self):
        return "{0}/{1}/{2}".format(self.month, self.day, self.year)

    __repr__ = __str__

    def __eq__(self, other):
        if self is other:
            return True
        if other is None:
            return False
        if not isinstance(other, Date):
            return False
        if self.year != other.year or self.month != other.month or self.day != other.day:
            return False
        return True


if __name__ == '__main__':
    date = Date(year=2017, month=12, day=24)
    print(date)

