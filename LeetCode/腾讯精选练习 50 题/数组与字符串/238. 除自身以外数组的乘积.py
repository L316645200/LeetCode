#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 238. 除自身以外数组的乘积.py
# @Author: Lin
# @Date  : 2022/5/1 17:50

# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 提示：
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s, on = 1, 0
        for n in nums:
            if n == 0:
                on += 1
            else:
                s *= n
        for i in range(len(nums)):
            if on >= 2 or (on == 1 and nums[i] != 0):
                nums[i] = 0
            elif nums[i] == 0:
                nums[i] = s
            else:
                nums[i] = int(s / nums[i])
        return nums


s = Solution()
s.productExceptSelf([1,2,3,4])