#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210904_剑指 Offer 10- I. 斐波那契数列.py
# @Author: Lin
# @Date  : 2021/9/4 9:43

# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：1
# 示例 2：
#
# 输入：n = 5
# 输出：5
#
# 提示：
#
# 0 <= n <= 100
from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        l = [0] * (n + 1)
        l[1] = 1
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[n] % 1000000007


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q

        return r


