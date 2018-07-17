#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 22:25
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : exercise_1.2.7.py
# @Software: PyCharm


def mystery(str):
    """
    序列倒序
    :rtype: str
    """
    length = len(str)
    if length <= 1:
        return str
    return mystery(str[length // 2:]) + mystery(str[:length // 2])


if __name__ == '__main__':
    print(mystery("abcdefg"))
    print(mystery([1,2,3,4,5,6,7]))