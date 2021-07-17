#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210716_剑指 Offer 53 - I. 在排序数组中查找数字 I.py
# @Author: Lin
# @Date  : 2021/7/17 15:41
# 统计一个数字在排序数组中出现的次数。
#
#  
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#  
#
# 限制：
#
# 0 <= 数组长度 <= 50000
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        r = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                r += 1
                left = mid - 1
                right = mid + 1
                while left >= 0 and nums[left] == target:
                    r += 1
                    left -= 1
                while right <= len(nums) - 1 and nums[right] == target :
                    r += 1
                    right += 1
                break
        return r