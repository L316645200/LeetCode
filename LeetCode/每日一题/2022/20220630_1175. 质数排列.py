#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220630_1175. 质数排列.py
# @Author: Lin
# @Date  : 2022/6/30 11:37

# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
# 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
# 示例 1：
# 输入：n = 5
# 输出：12
# 解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
# 示例 2：
# 输入：n = 100
# 输出：682289015
#
# 提示：
# 1 <= n <= 100
from math import sqrt


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        s = sum([self.is_prime(i) for i in range(1, n+1)])
        ans = 1
        for i in range(1, s+1):
            ans *= i
            ans %= 10 ** 9 + 7

        for i in range(1, n - s + 1):
            ans *= i
            ans %= 10 ** 9 + 7
        return ans

    def is_prime(self, n: int):
        if n == 1:
            return 0
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1


s = Solution()
s.numPrimeArrangements(100)