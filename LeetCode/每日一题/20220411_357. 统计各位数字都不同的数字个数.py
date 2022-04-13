#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220411_357. 统计各位数字都不同的数字个数.py
# @Author: Lin
# @Date  : 2022/4/11 9:43

# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
# 示例 1：
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。
# 示例 2：
# 输入：n = 0
# 输出：1
# 提示：
# 0 <= n <= 8
from functools import reduce


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        for i in range(1, n+1):
            s = reduce(lambda x,y: x*y, [j for j in range(9, 10-i, -1)] if 10-i < 9 else [1])
            res += 9*s
        return res

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
            print(cur, res)
        return res


s = Solution()
s.countNumbersWithUniqueDigits(3)