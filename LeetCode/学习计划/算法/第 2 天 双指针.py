#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 2 天 双指针.py
# @Author: Lin
# @Date  : 2021/7/23 16:59
# 977. 有序数组的平方
#
# 给你一个按
# 非递减顺序
# 排序的整数数组
# nums，返回
# 每个数字的平方
# 组成的新数组，要求也按
# 非递减顺序
# 排序。
#
# 示例
# 1：
#
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 解释：平方后，数组变为[16, 1, 0, 9, 100]
# 排序后，数组变为[0, 1, 9, 16, 100]
# 示例
# 2：
#
# 输入：nums = [-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]
#
# 提示：
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums
# 已按
# 非递减顺序
# 排序
#
# 进阶：
#
# 请你设计时间复杂度为
# O(n)
# 的算法解决本问题
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        i = right
        res = [0] * (i + 1)
        while i >= 0:

            if abs(nums[left]) >= abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
            i -= 1
        return res


# 189. 旋转数组
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 进阶：
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#  
#
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#  
# 提示：
#
# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums[:k], nums[k:] = nums[l-k:], nums[:l-k]




































