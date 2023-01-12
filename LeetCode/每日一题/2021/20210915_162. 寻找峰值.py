#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210915_162. 寻找峰值.py
# @Author: Lin
# @Date  : 2021/9/15 11:04
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1


s = Solution()
s.findPeakElement([3,4,3,2,1])