#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250126_40. 组合总和 II[medium].py
# @Author  ：Lin
# @Date    ：2025/1/27 11:44
"""40. 组合总和 II

给定一个候选人编号的集合candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。

示例1:
输入: candidates =[10,1,2,7,6,1,5], target =8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例2:
输入: candidates =[2,5,2,1,2], target =5,
输出:
[
[1,2,2],
[5]
]

提示:
	1 <=candidates.length <= 100
	1 <=candidates[i] <= 50
	1 <= target <= 30


https://leetcode.cn/problems/combination-sum-ii/description/?envType=daily-question&envId=2025-01-26"""
from typing import List



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)
        def dfs(i, arr, cur):
            if cur == target:
                ans.append(arr[:])
                return
            for j in range(i, n):
                if cur + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                dfs(j+1, arr + [candidates[j]], cur + candidates[j])
        dfs(0, [], 0)
        return ans

s = Solution()
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8,)
