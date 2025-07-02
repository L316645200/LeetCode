#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/13 12:59
# @Author  : Lin
# @File    : 20250613_2616. 最小化数对的最大差值[mid].py
"""2616. 最小化数对的最大差值 2155
给你一个下标从 0开始的整数数组nums和一个整数p。
请你从nums中找到p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的最大值最小。同时，你需要确保每个下标在这p个下标对中最多出现一次。
对于一个下标对i和j，这一对的差值为|nums[i] - nums[j]|，其中|x|表示 x的 绝对值。
请你返回 p个下标对对应数值 最大差值的 最小值。
示例 1：
输入：nums = [10,1,2,7,1,3], p = 2
输出：1
解释：第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
示例 2：
输入：nums = [4,2,1,2], p = 1
输出：0
解释：选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
提示：
	1 <= nums.length <= 10^5
	0 <= nums[i] <= 10^9
	0 <= p <= (nums.length)/2
https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/description/
"""
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1]
        while left <= right:
            mid = (right - left) // 2 + left
            i = cnt = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= mid:
                    i += 1
                    cnt += 1
                i += 1
            if cnt >= p:
                right = mid - 1
            else:
                left = mid + 1
        return left

s = Solution()
s.minimizeMax(nums = [10,1,2,7,1,3], p = 2)

# s.minimizeMax(nums = [4,2,1,2], p = 1)




















