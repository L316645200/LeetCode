#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230710_16. 最接近的三数之和.py
# @Author: Lin
# @Date  : 2023/7/17 14:46

# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 示例 1：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 提示：
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(best - target):
                    best = s
                if s == target:
                    return target
                if s - target > 0:
                    # 移动到下一个不相等的元素
                    while left < right - 1 and nums[right - 1] == nums[right]:
                        right -= 1
                    right = right - 1
                else:
                    while left + 1 < right and nums[left + 1] == nums[left]:
                        left += 1
                    left = left + 1

        return best


s = Solution()
s.threeSumClosest(nums = [-1,2,1,-4], target = 1)