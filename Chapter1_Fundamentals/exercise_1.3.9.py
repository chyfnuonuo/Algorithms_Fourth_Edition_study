#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 22:55
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.9.py
# @Software: PyCharm
from Chapter1_Fundamentals.stack import Stack


def spit_num(expr):
    result_list = []
    temp = ''
    for item in expr:

        if item in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            temp += item
        else:
            if len(temp) != 0:
                result_list.append(temp)
                temp = ''
            result_list.append(item)
    if len(temp) != 0:
        result_list.append(temp)
    return result_list


def parentheses(expr):
    stack = Stack()
    expr_list = spit_num(expr)
    for item in expr_list:
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
    print(parentheses('1+33)*21-1))'))

