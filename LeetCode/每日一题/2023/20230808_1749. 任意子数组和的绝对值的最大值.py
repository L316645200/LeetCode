#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230808_1749. 任意子数组和的绝对值的最大值.py
# @Author: Lin
# @Date  : 2023/8/8 11:08

# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。
# 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
# abs(x) 定义如下：
# 如果 x 是负整数，那么 abs(x) = -x 。
# 如果 x 是非负整数，那么 abs(x) = x 。
# 示例 1：
# 输入：nums = [1,-3,2,3,-4]
# 输出：5
# 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
# 示例 2：
# 输入：nums = [2,-5,1,-4,3,-2]
# 输出：8
# 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        positiveMax, negativeMin = 0, 0
        positiveSum, negativeSum = 0, 0

        for i in range(n):
            if positiveSum + nums[i] >= nums[i]:
                positiveSum += nums[i]
            else:
                positiveSum = nums[i]

            if negativeSum + nums[i] >= nums[i]:
                negativeSum = nums[i]
            else:
                negativeSum += nums[i]


            positiveMax = max(positiveMax, positiveSum)
            negativeMin = min(negativeMin, negativeSum)
        return max(abs(positiveMax), abs(negativeMin))


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positiveMax, negativeMin = 0, 0
        positiveSum, negativeSum = 0, 0
        for n in nums:
            positiveSum += n
            positiveMax = max(positiveMax, positiveSum)
            positiveSum = max(0, positiveSum)

            negativeSum += n
            negativeMin = min(negativeMin, negativeSum)
            negativeSum = min(0, negativeSum)

        return max(positiveMax, -negativeMin)


sol = Solution()
# sol.maxAbsoluteSum(nums = [-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9])
# sol.maxAbsoluteSum(nums = [1,-3,2,3,-4])

sol.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2])