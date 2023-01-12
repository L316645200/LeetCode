#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211009_441. 排列硬币.py
# @Author: Lin
# @Date  : 2021/10/12 9:53
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
#
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
#
#
# 示例 1：
#
#
# 输入：n = 5
# 输出：2
# 解释：因为第三行不完整，所以返回 2 。
# 示例 2：
#
#
# 输入：n = 8
# 输出：3
# 解释：因为第四行不完整，所以返回 3 。
#  
# 提示：
#
# 1 <= n <= 231 - 1
from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        arr = []
        s, t = 0, 0
        while s < n:
            t = t + 1
            s += t
            arr.append(t)
        return len(arr) if s == n else len(arr) - 1


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            ladder = (mid + 1) * (mid / 2)
            if ladder < n:
                left = mid + 1
            elif ladder > n:
                right = mid - 1
            else:
                return mid
        return right

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
            m = max(nums[i], m)
        return m
s = Solution()
m = s.maxSubArray(
[-2,1,-3,4,-1,2,1,-5,4])
print(m)
