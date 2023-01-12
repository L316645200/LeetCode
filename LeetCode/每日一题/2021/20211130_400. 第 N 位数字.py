#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211130_400. 第 N 位数字.py
# @Author: Lin
# @Date  : 2021/11/30 10:27
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。
#
# 示例 1：
# 输入：n = 3
# 输出：3
# 示例 2：
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#  
# 提示：
# 1 <= n <= 231 - 1


class Solution:
    def findNthDigit(self, n: int) -> int:
        ans, digit = 0, 0
        t = 0
        while ans <= n:
            t = (digit+1) * 9 * (10**digit)
            digit += 1
            ans += t
        ans -= t
        a, b = divmod(n - ans - 1, digit)
        if ans == n:
            digit += 1
        return int(str((10**(digit-1)) + a)[b])


s = Solution()
s.findNthDigit(189)