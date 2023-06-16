#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 3 天.py
# @Author: Lin
# @Date  : 2023/5/13 17:16

# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 提示：
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
# 进阶：
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
from typing import List
# 方法一：动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# 方法二：贪心 + 二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                left, right = 0, len(dp) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if dp[mid] >= num:
                        right = mid - 1
                    else:
                        left = mid + 1
                print(dp, left, right)
                dp[left] = num
        return len(dp)


s = Solution()
s.lengthOfLIS(nums = [7,7,7,7,7,7,7])

# 1760. 袋子里最少数目的球
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。
# 你可以进行如下操作至多 maxOperations 次：
# 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
# 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
# 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。
# 请你返回进行上述操作后的最小开销。
# 示例 1：
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
# 示例 2：
# 输入：nums = [2,4,8,2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
# 示例 3：
# 输入：nums = [7,17], maxOperations = 2
# 输出：7
# 提示：
# 1 <= nums.length <= 105
# 1 <= maxOperations, nums[i] <= 109


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left <= right:

            mid = left + (right - left) // 2
            operation = 0
            for num in nums:
                if num > mid:
                    operation += (num - 1) // mid
            if operation > maxOperations:
                left = mid + 1
            else:

                right = mid - 1
        return left



s = Solution()
s.minimumSize(nums = [9], maxOperations = 2)