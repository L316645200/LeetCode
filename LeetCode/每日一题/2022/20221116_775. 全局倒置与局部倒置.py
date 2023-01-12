#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221116_775. 全局倒置与局部倒置.py
# @Author: Lin
# @Date  : 2022/11/16 10:49

# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
# 0 <= i < j < n
# nums[i] > nums[j]
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [1,0,2]
# 输出：true
# 解释：有 1 个全局倒置，和 1 个局部倒置。
# 示例 2：
# 输入：nums = [1,2,0]
# 输出：false
# 解释：有 2 个全局倒置，和 1 个局部倒置。
# 提示：
# n == nums.length
# 1 <= n <= 105
# 0 <= nums[i] < n
# nums 中的所有整数 互不相同
# nums 是范围 [0, n - 1] 内所有数字组成的一个排列
from typing import List


# 暴力
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        g, l = 0, 0
        for i in range(n-1):
            for j in range(i+1, n):
                if j == i + 1 and nums[i] > nums[j]:
                    g, l = g + 1, l + 1
                elif nums[i] > nums[j]:
                    g += 1
        return l == g


# 后缀最小值，只要出现一次i大于后缀最小值即返回False
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [nums[n-1]] * n
        for i in range(n-2, -1, -1):
            arr[i] = min(nums[i], arr[i+1])
        for i in range(n-2):
            if nums[i] > arr[i+2]:
                return False
        return True


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = [nums[n-1]] * n
        for i in range(n-2, 0, -1):
            if nums[i-1] > arr[i+1]:
                return False
            arr[i] = min(nums[i], arr[i+1])

        return True

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))

s = Solution()
s.isIdealPermutation(nums = [2,0,3,1])