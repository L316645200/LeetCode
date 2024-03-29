#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230916_198. 打家劫舍.py
# @Author: Lin
# @Date  : 2023/9/16 9:42

"""你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n):
            if i < 3:
                dp[i] = nums[i] if i < 2 else dp[i-2] + nums[i]
            else:
                dp[i] = max(dp[i-3], dp[i-2]) + nums[i]

        return max(dp[-1], dp[-2])


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n >= 2:
            nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        return nums[n - 1]

s = Solution()
s.rob([2,1,1,2])