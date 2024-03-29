#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230809_1281. 整数的各位积和之差.py
# @Author: Lin
# @Date  : 2023/8/9 11:17

# 给你一个整数
# n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
# 示例
# 1：
# 输入：n = 234
# 输出：15
# 解释：
# 各位数之积 = 2 * 3 * 4 = 24
# 各位数之和 = 2 + 3 + 4 = 9
# 结果 = 24 - 9 = 15
# 示例
# 2：
# 输入：n = 4421
# 输出：21
# 解释：
# 各位数之积 = 4 * 4 * 2 * 1 = 32
# 各位数之和 = 4 + 4 + 2 + 1 = 11
# 结果 = 32 - 11 = 21
# 提示：
# 1 <= n <= 10 ^ 5


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        s = 0
        while n:
            x = n % 10
            n = n // 10
            m *= x
            s += x
        return m - s


s = Solution()
s.subtractProductAndSum(n = 234)