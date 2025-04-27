#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/19 15:33
# @Author  : Lin
# @File    : 20250419_2563. 统计公平数对的数目[medium].py

"""给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper


示例 1：

输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
示例 2：

输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。


提示：

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109"""
import bisect
from typing import List

# 双指针
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res, n = 0, len(nums)
        j = k = n - 1
        for i in range(n-1):
            if i >= j:
                break
            while j > i and nums[i] + nums[j] > upper:
                j -= 1
            while k > i and nums[i] + nums[k] >= lower:
                k -= 1
            res += j - max(i, k)
        return res

# 二分
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res, n = 0, len(nums)
        for i in range(n-1):
            j = bisect.bisect_right(nums, upper - nums[i], i + 1, n)
            k = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            res += j - k
        return res

s = Solution()
# s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
s.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
