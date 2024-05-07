#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240420_39. 组合总和.py
# @Author  ：Lin
# @Date    ：2024/4/20 14:32


"""给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。



示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []


提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40"""
from functools import cache
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        arr = []
        def dfs(l, i, s):
            for j in range(i, n):
                t = s + candidates[j]
                if t >= target:
                    if t == target:
                        arr.append(l + [candidates[j]])
                    break
                else:
                    dfs(l + [candidates[j]], j, t)
        dfs([], 0, 0)
        return arr


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(ans, target, index, size):
            if target < 0:
                return
            elif target == 0:
                res.append(ans)
                return
            for i in range(index, size):
                dfs(ans+[candidates[i]], target-candidates[i], i, size)

        res = []
        size = len(candidates)
        dfs([], target, 0, size)
        return res



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def dfs(arr, i, c):
            if i < 0:
                if c == 0:
                    ans.append(arr)
                return
            elif c >= candidates[i]:
                dfs(arr + [candidates[i]], i, c - candidates[i])
            dfs(arr, i - 1, c)

        dfs([], n - 1, target)
        return ans


s = Solution()
s.combinationSum(candidates = [2,3,5], target = 8)
