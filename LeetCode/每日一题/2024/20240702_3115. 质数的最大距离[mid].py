#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240702_3115. 质数的最大距离[mid].py
# @Author  ：Lin
# @Date    ：2024/7/2 9:23

"""给你一个整数数组 nums。
返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。
示例 1：
输入： nums = [4,2,9,5,3]
输出： 3
解释： nums[1]、nums[3] 和 nums[4] 是质数。因此答案是 |4 - 1| = 3。
示例 2：
输入： nums = [4,8,2,8]
输出： 0
解释： nums[2] 是质数。因为只有一个质数，所以答案是 |2 - 2| = 0。
提示：
1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
输入保证 nums 中至少有一个质数。"""
import math
from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

        left, right = 0, len(nums) - 1
        while left < len(nums):
            if is_prime(nums[left]):
                break
            left += 1
        while right >= 0:
            if is_prime(nums[right]):
                break
            right -= 1
        return right - left




s = Solution()
s.maximumPrimeDifference(nums = [4,2,9,5,3])