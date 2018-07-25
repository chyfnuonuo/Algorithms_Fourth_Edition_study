#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 21:34
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.10.py
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


def is_operator(item):
    if item in ('+', '-', '*', '/'):
        return True
    return False


def cmp_priority(item, param):
    if item in ('*', '/'):
        return True
    else:
        if param in ('*', '/'):
            return False
        else:
            return True


def is_num(item):
    if item in ('+', '-', '*', '/', '(', ')'):
        return False
    return True


def infix_to_prefix(expr):
    expr = spit_num(expr)[::-1]
    stack = Stack()
    result_list = []
    for item in expr:
        if is_num(item):
            result_list.append(item)
        elif item == ')':
            stack.push(item)
        elif is_operator(item):
            if stack.is_empty() or stack.peek() == ')' or cmp_priority(item, stack.peek()) > 0:
                stack.push(item)
            else:
                while True:
                    result_list.append(stack.pop())
                    if stack.is_empty() or stack.peek() == ')' or cmp_priority(item, stack.peek()) > 0:
                        stack.push(item)
                        break
        else:
            while stack.peek() != ')':
                result_list.append(stack.pop())
            stack.pop()
    while not stack.is_empty():
        result_list.append(stack.pop())
    return ' '.join(result_list[::-1])


if __name__ == '__main__':
    print(infix_to_prefix('(31+21)*33-31/17'))
