#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 22:12
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.16.py
# @Software: PyCharm
from math import gcd


class Rational(object):

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator can't be zero")
        common_divisor = gcd(numerator, denominator)

        self.__numerator = numerator // common_divisor
        self.__denominator = denominator // common_divisor

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

    __add__ = plus

    def minus(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        if self.denominator == other.denominator:
            return self.__class__(self.numerator - other.numerator, self.denominator)
        return self.__class__(self.numerator * other.denominator - other.numerator * self.denominator,
                              self.denominator * other.denominator)

    __sub__ = minus

    def times(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        return self.__class__(self.numerator * other.numerator, self.denominator * other.denominator)

    __mul__ = times

    def divides(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("parameter {0} must be {1}".format(other, self.__class__))
        if other.numerator == 0:
            raise ZeroDivisionError("denominator can't be zero")
        return self.__class__(self.numerator * other.denominator, self.denominator * other.numerator)

    __truediv__ = divides

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    __repr__ = __str__


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
