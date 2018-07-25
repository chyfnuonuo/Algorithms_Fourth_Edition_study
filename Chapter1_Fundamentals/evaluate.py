#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 19:50
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : evaluate.py
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

    return result_list


def evaluate(expr):
    oper_satck = Stack()
    vals_stack = Stack()
    expr_list = spit_num(expr)
    for item in expr_list:
        if item == "(":
            continue
        elif item in ['+', '-', '*', '/']:
            oper_satck.push(item)
        elif item == ")":
            op = oper_satck.pop()
            var = vals_stack.pop()
            if op == '+':
                var += vals_stack.pop()
            elif op == '-':
                var -= vals_stack.pop()
            elif op == '*':
                var *= vals_stack.pop()
            elif op == '/':
                var /= vals_stack.pop()
            else:
                pass
            vals_stack.push(var)
        else:
            vals_stack.push(float(item))
    return vals_stack.pop()


if __name__ == '__main__':
    print(evaluate("(1+11)"))
    print(evaluate("(((1+1)+((3*2)-4)/2)"))
