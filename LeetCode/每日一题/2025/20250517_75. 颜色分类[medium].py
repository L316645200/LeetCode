#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/17 9:23
# @Author  : Lin
# @File    : 20250517_75. 颜色分类[medium].py
"""给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]


提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2


进阶：

你能想出一个仅使用常数空间的一趟扫描算法吗？"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, left, right = 0, 0, n - 1
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1
s = Solution()
s.sortColors(nums = [2,1,2])
