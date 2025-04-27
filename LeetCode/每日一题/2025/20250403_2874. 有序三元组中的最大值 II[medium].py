#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/3 12:31
# @Author  : Lin
# @File    : 20250403_2874. 有序三元组中的最大值 II[medium].py

"""给你一个下标从 0 开始的整数数组 nums 。
请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。
下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。
示例 1：
输入：nums = [12,6,1,2,7]
输出：77
解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。
可以证明不存在值大于 77 的有序下标三元组。
示例 2：
输入：nums = [1,10,3,4,19]
输出：133
解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。
可以证明不存在值大于 133 的有序下标三元组。
示例 3：
输入：nums = [1,2,3]
输出：0
解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
提示：
3 <= nums.length <= 105
1 <= nums[i] <= 106"""
from typing import List

"""移动j，更新最大的i和k"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suf[i] = max(nums[i], suf[i+1])
        res, pre = 0, nums[0]
        for i in range(1, n):
            res = max(res, (pre - nums[i]) * suf[i+1])
            pre = max(pre, nums[i])
        return res


"""移动k，更新最大的j,记为maxpre,
更新最大的i-j,记为maxdiff"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = maxpre = maxdiff = 0
        for i in range(n):
            res = max(res, (maxdiff) * nums[i])
            maxpre = max(maxpre, nums[i])
            maxdiff = max(maxdiff, maxpre - nums[i])
        return res

s = Solution()
s.maximumTripletValue(nums = [12,6,1,2,7])
