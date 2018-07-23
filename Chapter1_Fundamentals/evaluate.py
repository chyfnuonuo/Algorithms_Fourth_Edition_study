#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 19:50
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : evaluate.py
# @Software: PyCharm
from Chapter1_Fundamentals.stack import Stack


def evaluate(expr):
    oper_satck = Stack()
    vals_stack = Stack()
    for item in expr:
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
    print(evaluate("(1+1)"))
    print(evaluate("(((1+1)+((3*2)-4)/2)"))
