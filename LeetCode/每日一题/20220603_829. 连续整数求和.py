#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220603_829. 连续整数求和.py
# @Author: Lin
# @Date  : 2022/6/6 14:34
# 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 
# 示例 1:
# 输入: n = 5
# 输出: 2
# 解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
# 示例 2:
# 输入: n = 9
# 输出: 3
# 解释: 9 = 4 + 5 = 2 + 3 + 4
# 示例 3:
# 输入: n = 15
# 输出: 4
# 解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 提示:
# 1 <= n <= 10^9​​​​​​​


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n < 3:
            return 1
        r = 0
        m = n * 2
        for i in range(1, int(m**(1/2))+1):
            j = m / i
            print(j)
            if j % 1 == 0:
                r += 1
                print(j)
        print(r)


s = Solution()
r = s.consecutiveNumbersSum(10)
print(r)
