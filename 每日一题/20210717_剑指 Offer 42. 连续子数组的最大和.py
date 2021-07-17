#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210717_剑指 Offer 42. 连续子数组的最大和.py
# @Author: Lin
# @Date  : 2021/7/17 15:35
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#  
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
#
# 提示：
#
# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = 0
        r = nums[0]
        for i in nums:
            m = max(m+i, i)
            r = max(r, m)
        return r