#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211104_367. 有效的完全平方数.py
# @Author: Lin
# @Date  : 2021/11/18 10:19
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
#
# 示例 1：
#
# 输入：num = 16
# 输出：true
# 示例 2：
#
# 输入：num = 14
# 输出：false
#
# 提示：
#
# 1 <= num <= 2^31 - 1


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 0
        while True:
            if n ** 2 == num:
                return True
            elif n ** 2 > num:
                return False
            n += 1


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


# 牛顿迭代法(狗都不看)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num

