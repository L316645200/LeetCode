#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/16 19:28
# @Author  : Lin
# @File    : 20250416_2537. 统计好子数组的数目[medium].py

"""给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中 好 子数组的数目。
一个子数组 arr 如果有 至少 k 对下标 (i, j) 满足 i < j 且 arr[i] == arr[j] ，那么称它是一个 好 子数组。
子数组 是原数组中一段连续 非空 的元素序列。
示例 1：
输入：nums = [1,1,1,1,1], k = 10
输出：1
解释：唯一的好子数组是这个数组本身。
示例 2：
输入：nums = [3,1,4,3,2,2,4], k = 2
输出：4
解释：总共有 4 个不同的好子数组：
- [3,1,4,3,2,2] 有 2 对。
- [3,1,4,3,2,2,4] 有 3 对。
- [1,4,3,2,2,4] 有 2 对。
- [4,3,2,2,4] 有 2 对。
提示：
1 <= nums.length <= 105
1 <= nums[i], k <= 109"""
from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = cnt = j = 0
        mp = defaultdict(int)
        n = len(nums)
        for i, num in enumerate(nums):
            cnt += mp[num]
            mp[num] += 1
            while cnt >= k:
                res += n - i
                mp[nums[j]] -= 1
                cnt -= mp[nums[j]]
                j += 1
        return res

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = cnt = j = 0
        mp = defaultdict(int)
        for i, num in enumerate(nums):
            cnt += mp[num]
            mp[num] += 1
            while cnt >= k:
                mp[nums[j]] -= 1
                cnt -= mp[nums[j]]
                j += 1
            res += j
        return res

s = Solution()
s.countGood(nums = [3,1,4,3,2,2,4], k = 2)
# s.countGood(nums = [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], k = 11)
