#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 三数之和.py
# @Author: Lin
# @Date  : 2021/7/10 11:09
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
# 提示：
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
# 相关标签
# 数组
# 双指针
# 排序
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        l = len(nums)
        # 长度不足3不满足
        if l < 3:
            return r

        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m, n = i + 1, l - 1
            t = nums[i] + nums[m] + nums[n]
            if t > 0 and nums[i] > 0:
                break
            # 双指针求解
            while m < n:
                if t < 0:
                    m += 1
                    while m < n and nums[m] == nums[m-1]:
                        m += 1
                elif t > 0:
                    n -= 1
                    while m < n and nums[n] == nums[n+1]:
                        n -= 1
                else:
                    r.append([nums[i], nums[m], nums[n]])
                    m += 1
                    n -= 1
                    while m < n and nums[m] == nums[m-1]:
                        m += 1
                    while m < n and nums[n] == nums[n+1]:
                        n -= 1
                t = nums[i] + nums[m] + nums[n]
        return r



s = Solution()
s.threeSum([-1,0,1,2,-1,-4])
