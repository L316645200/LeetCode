#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/7/16 20:51
# @Author  : Lin
# @File    : 20250716_3201. 找出有效子序列的最大长度 I[mid].py
"""给你一个整数数组 nums。
nums 的子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列：
(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2
返回 nums 的 最长的有效子序列 的长度。
一个 子序列 指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。
示例 1：
输入： nums = [1,2,3,4]
输出： 4
解释：
最长的有效子序列是 [1, 2, 3, 4]。
示例 2：
输入： nums = [1,2,1,1,2,1,2]
输出： 6
解释：
最长的有效子序列是 [1, 2, 1, 2, 1, 2]。
示例 3：
输入： nums = [1,3]
输出： 2
解释：
最长的有效子序列是 [1, 3]。
提示：
2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107"""
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化动态数组
        dp = [[1, 1] for _ in range(n)]
        # 相等数组的最大长度 idx[0]余数为0，idx[1]余数为1
        idx = [0, 0]
        idx[nums[0] % 2] += 1  # 首个数字余数
        ans = 1
        for i in range(1, n):
            dp[i][0] = idx[nums[i] % 2] + 1  # 相同数组的长度+1
            idx[nums[i] % 2] = dp[i][0]  # 更新idx
            dp[i][1] = dp[i - 1][1] + (nums[i] % 2 != nums[i - 1] % 2)  # 不同数组的最大长度
            ans = max(ans, max(dp[i]))
        return ans


s = Solution()
s.maximumLength(nums=[1, 2, 1, 1, 2, 1, 2])
