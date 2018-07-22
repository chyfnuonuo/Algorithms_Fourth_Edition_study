#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 22:12
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.16.py
# @Software: PyCharm


class Rational(object):

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator can't be zero")
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def plus(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        if self.denominator == other.denominator:
            return self.__class__(self.numerator + other.numerator, self.denominator)
        else:
            return self.__class__(self.numerator * other.denominator + other.numerator * self.denominator,
                                  self.denominator * other.denominator)

    def minus(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        if self.denominator == other.denominator:
            return self.__class__(self.numerator - other.numerator, self.denominator)
        return self.__class__(self.numerator * other.denominator - other.numerator * self.denominator,
                              self.denominator * other.denominator)

    def times(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        return self.__class__(self.numerator * other.numerator, self.denominator * other.denominator)

    def divides(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        if other.numerator == 0:
            raise ZeroDivisionError("denominator can't be zero")
        return self.__class__(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    __repr__ = __str__

    __add__ = plus

    __sub__ = minus

    __mul__ = times

    __truediv__ = divides


if __name__ == '__main__':
    num1 = Rational(-2, 3)
    num2 = Rational(-1, 3)
    print(num1)
    print(num1.plus(num2))
    print(num1.minus(num2))
    print(num1.times(num2))
    print(num1.divides(num2))
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
