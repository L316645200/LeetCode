#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天 二分查找.py
# @Author: Lin
# @Date  : 2021/7/22 12:17
# 704. 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#  
#
# 提示：
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

# 278. 第一个错误的版本
#
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
#
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
#
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
#
#  
# 示例 1：
#
# 输入：n = 5, bad = 4
# 输出：4
# 解释：
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true
# 所以，4 是第一个错误的版本。
# 示例 2：
#
# 输入：n = 1, bad = 1
# 输出：1
#  
#
# 提示：
# 1 <= bad <= n <= 231 - 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        r = n + 1
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                r = min(r, mid)
                right = mid - 1
            else:
                left = mid + 1
        return r


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