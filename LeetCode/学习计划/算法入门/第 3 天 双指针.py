#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 3 天 双指针.py
# @Author: Lin
# @Date  : 2021/7/24 10:51
# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

# 167. 两数之和 II - 输入有序数组
# 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
#
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
#
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#  
# 示例 1：
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
# 示例 2：
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
# 示例 3：
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
#
# 提示：
#
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers 按 递增顺序 排列
# -1000 <= target <= 1000
# 仅存在一个有效答案


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)
        while left < right:
            if numbers[left-1] + numbers[right-1] > target:
                right -= 1
            elif numbers[left-1] + numbers[right-1] < target:
                left += 1
            else:
                return [left, right]
