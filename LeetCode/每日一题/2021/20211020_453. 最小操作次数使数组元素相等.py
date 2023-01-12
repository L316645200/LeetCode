#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211020_453. 最小操作次数使数组元素相等.py
# @Author: Lin
# @Date  : 2021/10/20 10:04

# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
#  
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：3
# 解释：
# 只需要3次操作（注意每次操作会增加两个元素的值）：
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 示例 2：
#
# 输入：nums = [1,1,1]
# 输出：0
#
# 提示：
#
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 答案保证符合 32-bit 整数
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        res = 0
        for n in nums:
            res += n - minimum
        return res



s = Solution()
s.minMoves([1,2,3])