#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220214_540. 有序数组中的单一元素.py
# @Author: Lin
# @Date  : 2022/2/17 16:44

# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
# 请你找出并返回只出现一次的那个数。
# 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
#
# 示例 1:
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
# 示例 2:
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
# 提示:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
s = Solution()
s.singleNonDuplicate([3,3,7,7,10,11,11])
