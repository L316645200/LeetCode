#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 合并两个有序数组.py
# @Author: Lin
# @Date  : 2021/7/10 11:35
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 示例 2：
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
#
# 提示：
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[i] <= 109
# 相关标签
# 数组
# 双指针
# 排序
#
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        c = m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] >= nums2[b]:
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1