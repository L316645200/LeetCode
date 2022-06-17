#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 15. 三数之和.py
# @Author: Lin
# @Date  : 2022/5/1 10:14

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
#  
# 提示：
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l - 2):
            left, right = i + 1, l - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if left - 1 > i and nums[left] == nums[left - 1]:
                    left += 1
                elif nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return res


s = Solution()
res = s.threeSum([-2,0,0,2,2])