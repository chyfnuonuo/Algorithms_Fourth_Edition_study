#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 21:34
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.10.py
# @Software: PyCharm
from Chapter1_Fundamentals.stack import Stack


def cmp_high_priority(item, param):
    pass


def infix_to_postfix(expr):
    expr = expr[::-1]
    stack = Stack()
    result = ''
    for item in expr:
        if item in ('0','1','2','3','4','5','6','7','8','9'):
            result = result+item
        elif item == ')':
            stack.push(item)
        elif item in ('*','/','+','-'):
            while stack
            if stack.is_empty() or stack.peek()==')' or cmp_high_priority(item,stack.peek())>0:
                stack.push(item)

            elif




if __name__ == '__main__':
    pass
    
    