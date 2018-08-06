#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 22:14
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.11.py
# @Software: PyCharm
from Chapter1_Fundamentals.bagqueuestack.stack import Stack


def is_num(item):
    if item.isdigit():
        result = True
    else:
        try:
            float(item)
        except ValueError:
            result = False
        else:
            result = True

    return result


def spit_num(expr):
    result_list = []
    temp = ''
    for item in expr:

        if item.isdigit() or item == '.':
            temp += item
        elif is_operator(item):
            if len(temp) != 0:
                result_list.append(temp)
                temp = ''
            result_list.append(item)
        else:
            if len(temp) != 0:
                result_list.append(temp)
                temp = ''
            continue
    if len(temp) != 0:
        result_list.append(temp)
    return result_list


def is_operator(item):
    if item in ('+', '-', '*', '/'):
        return True
    return False


def cal(operator1, operator2, item):
    if item == '+':
        return operator1 + operator2
    elif item == '-':
        return operator1 - operator2
    elif item == '*':
        return operator1 * operator2
    else:
        return operator1 / operator2


def evaluate_postfix(expr):
    expr_list = spit_num(expr)
    stack = Stack()
    for item in expr_list:
        if is_num(item):
            stack.push(item)
        elif is_operator(item):
            operator2 = stack.pop()
            operator1 = stack.pop()
            result = cal(float(operator1), float(operator2), item)
            stack.push(result)
        else:
            raise ValueError
    return stack.pop()


if __name__ == '__main__':
    print(evaluate_postfix('1 1 + 1 * 1 2 / -'))
