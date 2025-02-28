#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250206_47. 全排列 II[medium].py
# @Author  ：Lin
# @Date    ：2025/2/6 9:15
"""47. 全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：
	1 <= nums.length <= 8
	-10 <= nums[i] <= 10


https://leetcode.cn/problems/permutations-ii/description/?envType=daily-question&envId=2025-02-06"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        visited = [False] * n
        def backtrack(arr):
            if len(arr) == n:
                ans.append(arr[:])
                return
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                backtrack(arr + [nums[i]])
                visited[i] = False
        backtrack([])
        return ans

s = Solution()
s.permuteUnique(nums = [1,1,2])
