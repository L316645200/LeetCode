#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220611_926. 将字符串翻转到单调递增.py
# @Author: Lin
# @Date  : 2022/6/11 10:56
# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
# 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
# 返回使 s 单调递增的最小翻转次数。
# 示例 1：
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
# 示例 2：
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
# 示例 3：
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。
# 提示：
#
# 1 <= s.length <= 105
# s[i] 为 '0' 或 '1'
#
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)
s = Solution()
s.minFlipsMonoIncr( "001001")