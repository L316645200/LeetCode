#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250205_90. 子集 II[medium].py
# @Author  ：Lin
# @Date    ：2025/2/5 9:47

"""90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
提示：
	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
https://leetcode.cn/problems/subsets-ii/description/?envType=daily-question&envId=2025-02-05"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def dfs(i, path):
            ans.append(path[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(j + 1, path + [nums[j]])
        dfs(0, [])
        return ans
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        path = []
        def dfs(i):
            ans.append(path[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans

s = Solution()
s.subsetsWithDup(nums = [1,2,2,3])
