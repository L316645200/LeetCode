#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20210708_930. 和相同的二元子数组.py
# @Author: Lin
# @Date  : 2021/7/10 12:19
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
#
# 子数组 是数组的一段连续部分。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,0,1,0,1], goal = 2
# 输出：4
# 解释：
# 有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
# 示例 2：
#
# 输入：nums = [0,0,0,0,0], goal = 0
# 输出：15
#  
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# nums[i] 不是 0 就是 1
# 0 <= goal <= nums.length


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        n = 0

        for i in range(len(nums)):
            if i > 0:
                nums[i] = nums[i] + nums[i - 1]

            n += d[nums[i] - goal]

            d[nums[i]] += 1
        return n