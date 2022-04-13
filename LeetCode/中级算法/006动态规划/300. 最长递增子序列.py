#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 300. 最长递增子序列.py
# @Author: Lin
# @Date  : 2022/4/12 14:43
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
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
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [float('inf')]
        print(arr)

        for num in nums:
            if num > arr[-1]:
                arr.append(num)
            else:
                n = bisect.bisect_left(arr, num)
                arr[n] = num
        return len(arr)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         l = len(nums)
#         dp = [1] * l
#         r = 0
#
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         d = []
#         for n in nums:
#             if not d or n > d[-1]:
#                 d.append(n)
#             else:
#                 l, r = 0, len(d) - 1
#                 loc = r
#                 while l <= r:
#                     mid = (l + r) // 2
#                     if d[mid] >= n:
#                         loc = mid
#                         r = mid - 1
#                     else:
#                         l = mid + 1
#                 d[loc] = n
#         return len(d)
sol = Solution()
sol.lengthOfLIS([10,9,2,5,3,7,101,18])