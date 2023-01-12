#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20221024_915. 分割数组.py
# @Author: Lin
# @Date  : 2022/10/24 11:32

# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 的长度要尽可能小。
# 在完成这样的分组后返回 left 的 长度 。
# 用例可以保证存在这样的划分方法。
# 示例 1：
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
# 示例 2：
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
# 提示：
# 2 <= nums.length <= 105
# 0 <= nums[i] <= 106
# 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        mini_arr = [0] * n
        mini_arr[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            mini_arr[i] = min(nums[i], mini_arr[i+1])

        for i in range(n-1):
            maxi = max(maxi, nums[i])
            if maxi <= mini_arr[i+1]:
                return i+1


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans, curr_maxi, maxi = 1, nums[0], nums[0]

        for i in range(1, len(nums)-1):
            curr_maxi = max(curr_maxi, nums[i])
            if nums[i] < maxi:
                ans = i + 1
                maxi = curr_maxi
        return ans


s = Solution()
s.partitionDisjoint(nums = [90,47,69,10,43,92,31,73,61,97])

s.partitionDisjoint(nums = [1,1])
