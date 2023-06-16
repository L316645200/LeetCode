#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 11 天.py
# @Author: Lin
# @Date  : 2023/4/17 17:17

# 1855. 下标对中的最大距离
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left, right = len(nums1) - 1, len(nums2) - 1
        ans = 0

        for i in range(left, -1, -1):
            if right < i:
                continue
            while right >= 0 and nums2[right] < nums1[i]:
                right -= 1
            if right >= i:
                ans = max(ans, right - i)
        return ans

s = Solution()
s.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5])

# 33. 搜索旋转排序数组