#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241104_633. 平方数之和[medium].py
# @Author  ：Lin
# @Date    ：2024/11/4 14:49


"""给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。



示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false


提示：

0 <= c <= 231 - 1"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(int(math.sqrt(c))+1):
            j = math.sqrt(c - i ** 2)

            if int(j) == j:
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left ** 2 + right ** 2 == c:
                return True
            elif left ** 2 + right ** 2 > c:
                right -= 1
            else:
                left += 1
        return False

s = Solution()
r = s.judgeSquareSum(2)
print(r)
