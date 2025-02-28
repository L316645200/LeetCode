#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250129_219. 存在重复元素 II[easy].py
# @Author  ：Lin
# @Date    ：2025/2/5 17:23

"""219. 存在重复元素 II

给你一个整数数组nums 和一个整数k ，判断数组中是否存在两个 不同的索引i和j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。

示例1：
输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false

提示：
	1 <= nums.length <= 10^5
	-10^9 <= nums[i] <= 10^9
	0 <= k <= 10^5


https://leetcode.cn/problems/contains-duplicate-ii/?envType=daily-question&envId=2025-01-29"""
from typing import List

# 哈希
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp and i - mp[num] <= k:
                return True
            mp[num] = i
        return False
# 哈希+滑动
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = set()
        for i, num in enumerate(nums):
            if num in mp:
                return True
            mp.add(num)
            if i >= k:
                mp.remove(nums[i-k])
        return False



s = Solution()
s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
