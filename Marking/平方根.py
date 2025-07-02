#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 平方根.py
# @Author: Lin
# @Date  : 2021/10/15 17:51


def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x/y)/2
        # y = x/y
        print(y)
    return y

sqrt(9)

