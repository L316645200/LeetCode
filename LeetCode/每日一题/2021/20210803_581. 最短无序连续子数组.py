#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210803_581. 最短无序连续子数组.py
# @Author: Lin
# @Date  : 2021/8/3 11:18
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 示例 2：
#
# 输入：nums = [1,2,3,4]
# 输出：0
# 示例 3：
#
# 输入：nums = [1]
# 输出：0
#  
#
# 提示：
#
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
#  
#
# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
            print(maxn, minn)
        return 0 if right == -1 else right - left + 1


s = Solution()
s.findUnsortedSubarray([2,6,4,8,10,9,15])