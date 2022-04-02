#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 计数质数.py
# @Author: Lin
# @Date  : 2021/7/10 11:48
# 统计所有小于非负整数 n 的质数的数量。
#
#  
#
# 示例 1：
#
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 示例 2：
#
# 输入：n = 0
# 输出：0
# 示例 3：
#
# 输入：n = 1
# 输出：0
#  
#
# 提示：
#
# 0 <= n <= 5 * 106
# 相关标签
# 数组
# 数学
# 枚举
# 数论

class Solution:
    def countPrimes(self, n: int) -> int:
        r = 0
        is_primes = [True] * (n+1)
        for i in range(2, n):
            if is_primes[i]:
                r += 1
                for j in range(2,n//i+1):
                    is_primes[i*j] = False
        return r