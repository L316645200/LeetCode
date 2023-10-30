#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230917_213. 打家劫舍 II.py
# @Author: Lin
# @Date  : 2023/9/18 15:31

"""你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。



示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [1,2,3]
输出：3


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000"""
from typing import List

#
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[]] * n
        # 选择第一间和不选第一间的最大值
        dp[0] = [nums[0], 0]

        if n >= 2:
            dp[1] = [nums[0], nums[1]]

        for i in range(2, n):

            if i != n-1:
                dp[i] = [max(dp[i-2][0] + nums[i], dp[i-1][0]), max(dp[i-2][1] + nums[i], dp[i-1][1])]
            else:
                dp[i] = [max(dp[i-2][0], dp[i-1][0]), max(dp[i-2][1] + nums[i], dp[i-1][1])]
        return max(dp[n-1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        selected, notselected = [nums[0], 0], [0, 0]

        for i in range(1, n):
            if i != n-1:
                selected = [max(selected[1] + nums[i], selected[0]), selected[0]]
            else:
                selected = [max(selected[1], selected[0]), selected[0]]
            notselected = [max(notselected[1] + nums[i], notselected[0]), notselected[0]]
        return max(selected[0], notselected[0])

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start+1])
            for i in range(start+2, end+1):
                first, second = second, max(nums[i] + first, second)
            return second

        if n <= 3:
            return max(nums)
        # 选第一间则是求0-n-1间的最大值，不选第一间是求1-n间的最大值
        return max(robRange(0, n-2), robRange(1, n-1))


s = Solution()
s.rob(nums = [2,1])