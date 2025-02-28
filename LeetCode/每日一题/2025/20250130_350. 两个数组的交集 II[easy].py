#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250130_350. 两个数组的交集 II[easy].py
# @Author  ：Lin
# @Date    ：2025/2/5 17:37
"""350. 两个数组的交集 II

给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

提示：
	1 <= nums1.length, nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 1000
进阶：
	如果给定的数组已经排好序呢？你将如何优化你的算法？
	如果nums1的大小比nums2 小，哪种方法更优？
	如果nums2的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2025-01-30"""
from collections import Counter
from typing import List

# 排序+双指针
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i = j = 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

# 计数
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        ans = []
        for c, v in cnt1.items():
            if c in cnt2:
                for i in range(min(cnt2[c], v)):
                    ans.append(c)
        return ans

s = Solution()
s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
