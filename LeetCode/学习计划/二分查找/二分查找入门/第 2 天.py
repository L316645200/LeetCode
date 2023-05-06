#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 2 天.py
# @Author: Lin
# @Date  : 2023/3/10 18:29

 # 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
# 示例 4:
#
# 输入: nums = [1,3,5,6], target = 0
# 输出: 0
# 示例 5:
#
# 输入: nums = [1], target = 0
# 输出: 0
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left

s =Solution()
s.searchInsert(nums = [1,3,5,6], target = 5)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] > target:
            return 0
        elif nums[right] < target:
            return right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left

# 852. 山脉数组的峰顶索引
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。
# 示例 1：
# 输入：arr = [0,1,0]
# 输出：1
# 示例 2：
# 输入：arr = [0,2,1,0]
# 输出：1
# 示例 3：
# 输入：arr = [0,10,5,2]
# 输出：1
# 示例 4：
# 输入：arr = [3,4,5,1]
# 输出：2
# 示例 5：
# 输入：arr = [24,69,100,99,79,78,67,36,26,19]
# 输出：2
# 提示：
# 3 <= arr.length <= 104
# 0 <= arr[i] <= 106
# 题目数据保证 arr 是一个山脉数组
# 进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif mid == 0:
                return 1
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
s.peakIndexInMountainArray(arr = [3,9,8,6,4])


































