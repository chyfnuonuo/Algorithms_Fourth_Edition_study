#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 22:16
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.3.4.py
# @Software: PyCharm
from Chapter1_Fundamentals.stack import Stack


def parentheses(expr):
    stack = Stack()
    dic = {')': '(', ']': '[', '}': '{'}
    result = True
    for item in expr:
        if item in dic.values():
            stack.push(item)
        elif item in dic.keys():
            try:
                if stack.pop() != dic[item]:
                    result = False
            except EOFError:
                result = False
        else:
            raise ValueError
    if not stack.is_empty():
        result = False
    return result


if __name__ == '__main__':
    print(parentheses('{[{{{'))
    print(parentheses('{}[{}[]]'))
    print(parentheses('}[{}[]]'))
