#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 300. 最长递增子序列.py
# @Author: Lin
# @Date  : 2021/7/27 9:31
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#  
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
#
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#  
# 进阶：
#
# 你可以设计时间复杂度为 O(n2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
from typing import List


# 动态规划 O(n**2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                print(i,j,dp)
        return max(dp)

s = Solution()
s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
# 二分 O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                    print(n, d, l, r, mid, loc)
                d[loc] = n
            print(d)
        return len(d)
