#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Fizz Buzz.py
# @Author: Lin
# @Date  : 2021/7/10 11:48
# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
#
# 2. 如果 n 是5的倍数，输出“Buzz”；
#
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
# 示例：
#
# n = 15,
#
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
# 相关标签
# 数学
# 字符串
# 模拟
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                r.append('FizzBuzz')
            elif i % 5 == 0:
                r.append('Buzz')
            elif i % 3 == 0:
                r.append('Fizz')
            else:
                r.append(str(i))
        return r