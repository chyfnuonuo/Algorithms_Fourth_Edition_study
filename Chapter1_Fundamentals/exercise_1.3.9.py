#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 22:55
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.9.py
# @Software: PyCharm
from Chapter1_Fundamentals.stack import Stack


def parentheses(expr):
    stack = Stack()
    for item in expr:
        if item == ')':
            num1 = stack.pop()
            oper = stack.pop()
            num2 = stack.pop()
            temp = '(' + num2 + oper + num1 + ')'
            stack.push(temp)
        else:
            stack.push(item)
    return stack.pop()


if __name__ == '__main__':
    print(parentheses('1+3)*2-1))'))
