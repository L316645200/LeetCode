#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/28 10:30
# @Author  : Lin
# @File    : 20250428_2302. 统计得分小于 K 的子数组数目[hard].py
"""一个数组的 分数 定义为数组之和 乘以 数组的长度。

比方说，[1, 2, 3, 4, 5] 的分数为 (1 + 2 + 3 + 4 + 5) * 5 = 75 。
给你一个正整数数组 nums 和一个整数 k ，请你返回 nums 中分数 严格小于 k 的 非空整数子数组数目。

子数组 是数组中的一个连续元素序列。



示例 1：

输入：nums = [2,1,4,3,5], k = 10
输出：6
解释：
有 6 个子数组的分数小于 10 ：
- [2] 分数为 2 * 1 = 2 。
- [1] 分数为 1 * 1 = 1 。
- [4] 分数为 4 * 1 = 4 。
- [3] 分数为 3 * 1 = 3 。
- [5] 分数为 5 * 1 = 5 。
- [2,1] 分数为 (2 + 1) * 2 = 6 。
注意，子数组 [1,4] 和 [4,3,5] 不符合要求，因为它们的分数分别为 10 和 36，但我们要求子数组的分数严格小于 10 。
示例 2：

输入：nums = [1,1,1], k = 5
输出：5
解释：
除了 [1,1,1] 以外每个子数组分数都小于 5 。
[1,1,1] 分数为 (1 + 1 + 1) * 3 = 9 ，大于 5 。
所以总共有 5 个子数组得分小于 5 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 1015"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = j = t = 0
        for i, x in enumerate(nums):
            t += x
            while t * (i - j + 1) >= k:
                t -= nums[j]
                j += 1
            ans += i - j + 1
        return ans


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # s 滑动数组的和
        # left， right 滑动数组的左右指针
        ans = left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans

s = Solution()
s.countSubarrays(nums = [2,1,4,3,5], k = 10)
