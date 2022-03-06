#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 21:52
# @Author  : leo cheng
# @Email   : chengyoufu@163.com
# @File    : func_utils.py
# @Software: PyCharm
import functools


def type_check_deco(*check_types):
    """

    :param chenc_types:
    :return:we
    """

    def check(func):
        @functools.wraps(func)
        def warps(*args, **kwargs):
            for param, check_type in zip(args, check_types):
                if not isinstance(param,check_type):
                    raise TypeError("param {0} must be {1} type  ".format(param, check_type))

            return func(*args, **kwargs)

        return warps

    return check


if __name__ == '__main__':
    pass
