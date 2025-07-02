#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/10 15:25
# @Author  : Lin
# @File    : 20250510_2918. 数组的最小相等和[medium].py

"""给你两个由正整数和 0 组成的数组 nums1 和 nums2 。

你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。

返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。



示例 1：

输入：nums1 = [3,2,0,1,0], nums2 = [6,5,0]
输出：12
解释：可以按下述方式替换数组中的 0 ：
- 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。
- 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。
两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。
示例 2：

输入：nums1 = [2,0,2,0], nums2 = [1,4]
输出：-1
解释：无法使两个数组的和相等。


提示：

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[i] <= 106"""
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        c1, c2 = nums1.count(0), nums2.count(0)
        if c1 > 0 and c2 > 0:
            return max(s1 + c1, s2 + c2)
        elif c2 > 0 and s1 >= s2 + c2:
            return s1
        elif c1 > 0 and s2 >= s1 + c1:
            return s2
        elif c1 == c2 == 0 and s1 == s2:
            return s1
        return -1

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(max(x, 1) for x in nums1), sum(max(x, 1) for x in nums2)
        if s1 < s2 and 0 not in s1 or s1 > s2 and 0 not in s2:
            return -1
        return max(s1, s2)


s = Solution()
r = s.minSum(nums1 = [17,1,13,12,3,13],
         nums2 = [2,25])
print(r)