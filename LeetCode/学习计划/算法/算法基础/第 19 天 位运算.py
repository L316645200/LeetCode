#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 19 天 位运算.py
# @Author: Lin
# @Date  : 2022/8/24 16:47

# 201. 数字范围按位与
# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
# 示例 1：
# 输入：left = 5, right = 7
# 输出：4
# 示例 2：
# 输入：left = 0, right = 0
# 输出：0
# 示例 3：
# 输入：left = 1, right = 2147483647
# 输出：0
# 提示：
#
# 0 <= left <= right <= 231 - 1


# TODO 还是看不懂
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
            print(n)
        return n

s = Solution()
s.rangeBitwiseAnd(m = 5, n = 7)