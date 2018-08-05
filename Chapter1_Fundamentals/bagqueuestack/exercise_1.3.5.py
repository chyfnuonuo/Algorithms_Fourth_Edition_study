#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 23:14
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.5.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.link_list import LinkList, Node
from Chapter1_Fundamentals.bagqueuestack.stack import Stack


def convert_binary(num):
    """
    把十进制数字转换为二进制
    :param num: 需要转换的数字
    :return:
    """
    stack = Stack()
    while num > 0:
        stack.push(num % 2)
        num = num // 2
    result = 0
    while not stack.is_empty():
        result = result * 10 + stack.pop()
    return result


def convert(num, base=2):
    digits = '0123456789ABCDEF'
    stack = Stack()
    while num > 0:
        stack.push(num % base)
        num = num // base
    result = ''
    while not stack.is_empty():
        result = result + digits[stack.pop()]
    return result


if __name__ == '__main__':
    print(convert_binary(50))
    print(convert_binary(4))
    print(convert_binary(2))
    print(convert(2))
    print(convert(15))
    print(convert(16, base=16))
    print(convert(63524, base=16))
