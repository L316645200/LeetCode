#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230422_1027. 最长等差数列.py
# @Author: Lin
# @Date  : 2023/4/22 11:15
from typing import List

# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
# 示例 1：
# 输入：nums = [3,6,9,12]
# 输出：4
# 解释：
# 整个数组是公差为 3 的等差数列。
# 示例 2：
# 输入：nums = [9,4,7,2,10]
# 输出：3
# 解释：
# 最长的等差子序列是 [4,7,10]。
# 示例 3：
# 输入：nums = [20,1,15,3,10,5,8]
# 输出：4
# 解释：
# 最长的等差子序列是 [20,15,10,5]。
# 提示：
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        diff = max_num - min_num
        ans = 0
        for d in range(-diff, diff+1):
            f = dict()
            for num in nums:
                if (prev := num - d) in f:
                    f[num] = max(f.get(num, 0), f[prev] + 1)
                    ans = max(f[num], ans)

                f[num] = max(f.get(num, 0), 1)
        return ans
s = Solution()
s.longestArithSeqLength(nums = [20,1,15,3,10,5,8])

