#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211231_507. 完美数.py
# @Author: Lin
# @Date  : 2021/12/31 10:00
# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
#
#  
#
# 示例 1：
#
# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。
# 示例 2：
#
# 输入：num = 6
# 输出：true
# 示例 3：
#
# 输入：num = 496
# 输出：true
# 示例 4：
#
# 输入：num = 8128
# 输出：true
# 示例 5：
#
# 输入：num = 2
# 输出：false
#  
#
# 提示：
#
# 1 <= num <= 108

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        d = 2
        ans = 1
        while d * d <= num:
            if num % d == 0:
                ans += num // d + d
            d += 1
        return ans == num


# 2**(p-1)*(2**p-1)  p为素数2**p-1也是素数

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336


s = Solution()
s.checkPerfectNumber(28)

p = 1
while p <= 15:
    n = (2 ** (p - 1)) * (2 ** p - 1)
    print(p, n)
    p += 1
