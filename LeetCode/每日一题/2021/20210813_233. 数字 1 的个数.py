#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210813_233. 数字 1 的个数.py
# @Author: Lin
# @Date  : 2021/8/13 15:07
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#  
#
# 示例 1：
#
# 输入：n = 13
# 输出：6
# 示例 2：
#
# 输入：n = 0
# 输出：0
#  
#
# 提示：
#
# 0 <= n <= 2 * 109

class Solution:
    def countDigitOne(self, n: int) -> int:
        l = len(str(n))
        ans = 0
        for i in range(l):
            t = 10 ** i
            # 每次表示该位上的1出现的次数
            # n // (t*10) * 10 表示左边位数 决定该位的1个数
            # n % (t*10) - t + 1 表示溢出的1的个数，最小为0，最大为 t
            ans += n // (t*10) * t + min(t, max(0, n % (t*10) - t + 1))
        return ans
s = Solution()
s.countDigitOne(100)