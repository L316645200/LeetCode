#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211006_414. 第三大的数.py
# @Author: Lin
# @Date  : 2021/10/11 10:17
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
#
# 示例 1：
#
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。
# 示例 2：
#
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
# 示例 3：
#
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
#  
#
# 提示：
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#  
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        return nums[2] if len(nums) >= 3 else nums[0]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = [float("-inf"), float("-inf"), float("-inf")]
        nums = set(nums)
        for n in nums:
            if n > arr[0]:
                arr[0], arr[1], arr[2] = n, arr[0], arr[1]
            elif n > arr[1]:
                arr[1], arr[2] = n, arr[1]
            elif n > arr[2]:
                arr[2] = n
        return arr[2] if arr[2] > float("-inf") else arr[0]


so = Solution()
arr = so.thirdMax([1,2,-2147483648])

