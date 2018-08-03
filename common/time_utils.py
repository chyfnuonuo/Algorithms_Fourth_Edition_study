#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/8 21:47
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : time_utils.py
# @Software: PyCharm
import functools

import time


def time_elapsed_deco(func):
    """
    包含了装饰器函数wrapper，用来修改所装饰函数的行为
    :param func: 所装饰的函数
    :return: 装饰器函数
    """

    @functools.wraps(func)  # 自动拷贝元信息到装饰器
    def wrapper(*args, **kwargs):
        """
        用于计算时间的装饰器
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        msecs = (end_time - start_time)
        print("{0}>>elapsed time:{1} ms".format(func.__name__, msecs))
        return result

    return wrapper


if __name__ == '__main__':
    pass
