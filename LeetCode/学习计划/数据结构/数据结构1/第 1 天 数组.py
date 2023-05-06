#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天 数组.py
# @Author: Lin
# @Date  : 2021/10/21 15:59
# 217. 存在重复元素
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
#  
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# 53. 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#  
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
# 示例 4：
#
# 输入：nums = [-1]
# 输出：-1
# 示例 5：
#
# 输入：nums = [-100000]
# 输出：-100000
#  
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#  
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i]+nums[i-1],nums[i])
            s = max(nums[i], s)
        return s