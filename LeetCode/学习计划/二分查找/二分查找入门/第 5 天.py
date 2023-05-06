#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 5 天.py
# @Author: Lin
# @Date  : 2023/4/7 17:28

# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 是一个非递减数组
# -109 <= target <= 109
#
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        left = search_left(nums, target)
        right = search_right(nums, target)
        return [left, right] if left <= right else [-1, -1]




class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int, lower: bool) -> int:
            left, right = 0, len(nums) - 1
            ans = len(nums)
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] > target or (lower and nums[mid] == target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans

        left = binary_search(nums, target, False)
        right = binary_search(nums, target, True) - 1
        if left <= right and  right < len(nums) and nums[left] == target == nums[right]:
            return [left, right]
        return [-1, -1]

s = Solution()
s.searchRange(nums = [5,7,7,8,8,10], target = 8)

s.searchRange(nums = [], target = 0)