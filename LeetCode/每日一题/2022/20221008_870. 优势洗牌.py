#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221008_870. 优势洗牌.py
# @Author: Lin
# @Date  : 2022/10/10 16:38

# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。
# 示例 1：
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
# 示例 2：
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
# 提示：
# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [0] * n
        nums1_sort = sorted(nums1)
        nums2_sort = sorted(enumerate(nums2), key=lambda x: x[1])
        l, r = 0, n - 1
        for i in range(n):
            if nums1_sort[i] > nums2_sort[l][1]:
                ans[nums2_sort[l][0]] = nums1_sort[i]
                l += 1
            else:
                ans[nums2_sort[r][0]] = nums1_sort[i]
                r -= 1
        return ans


s = Solution()
s.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11])


s.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11])