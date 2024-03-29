#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220519_462. 最少移动次数使数组元素相等 II.py
# @Author: Lin
# @Date  : 2022/5/19 15:43

# 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
# 在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：2
# 解释：
# 只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 示例 2：
# 输入：nums = [1,10,2,9]
# 输出：16
# 提示：
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum([abs(n - nums[len(nums)//2]) for n in nums])


s = Solution()
s.minMoves2([1,10,2,9])
