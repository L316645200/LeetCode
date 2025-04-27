#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/7 17:26
# @Author  : Lin
# @File    : 20250407_416. 分割等和子集[medium].py
"""给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        m = sum(nums)
        if m % 2 == 1:
            return False
        m //= 2
        dp = [[0] * (m + 1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if j + 1 >= nums[i]:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i][j+1-nums[i]] + nums[i])
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1] == m


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        if m % 2 == 1:
            return False
        m //= 2
        dp = [0] * (m + 1)

        for i, num in enumerate(nums):
            for j in range(m-1, -1, -1):
                if j + 1 >= num:
                    dp[j+1] = max(dp[j+1], dp[j+1-num] + num)
        return dp[-1] == m


s = Solution()
# s.canPartition(nums = [1,5,11,5])
s.canPartition(nums = [1,5,10,6])
