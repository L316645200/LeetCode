#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 10 天 递归_回溯.py
# @Author: Lin
# @Date  : 2022/7/25 17:32

# 46. 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]
# 提示：
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
from collections import Counter
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(arr):
            if len(arr) == n:
                res.append(arr)
                return
            for i in range(n):
                if nums[i] in arr:
                    continue
                # arr.append(nums[i])
                backtrack(arr + [nums[i]])
                # arr.pop()

        backtrack([])
        print(res)
        return res
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        check = [0] * n

        def backtrack(arr):
            if len(arr) == n:
                res.append(arr)
                return
            for i in range(n):
                if check[i] == 1:
                    continue
                # arr.append(nums[i])
                check[i] = 1
                backtrack(arr + [nums[i]])
                check[i] = 0
                # arr.pop()

        backtrack([])
        print(res)
        return res


s = Solution()
s.permute(nums = [1,2,3])

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def hastack(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                hastack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        hastack(nums, [])
        print(res)
        return res



# 47. 全排列 II
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 提示：
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        check = [0] * n
        nums.sort()
        def hastack(arr):
            if len(arr) == n:
                res.append(arr)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                # 剪枝
                # check[i-1] == 1 和 check[i-1] == 0都可以，check[i-1] == 0在前一层就剪枝
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                hastack(arr + [nums[i]])
                check[i] = 0

        hastack([])
        return res


s = Solution()
s.permuteUnique(nums = [3,3,0,3])


# 39. 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例 2：
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：
# 输入: candidates = [2], target = 1
# 输出: []
# 提示：
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都 互不相同
# 1 <= target <= 500
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


s = Solution()
s.combinationSum(candidates = [2,3,5], target = 8)

# 40. 组合总和 II
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。 
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 提示:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        n = len(candidates)
        check = [0] * n

        def dfs(ans, target, index, size):
            if target < 0:
                return
            elif target == 0:
                res.append(ans)
                return
            for i in range(index, size):
                # 剪枝
                if i > 0 and candidates[i] == candidates[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                dfs(ans + [candidates[i]], target - candidates[i], i+1, size)
                check[i] = 0

        dfs([], target, 0, n)
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(ans, target, index, size):
            for i in range(index, size):
                poor = target - candidates[i]
                if poor < 0:
                    break
                elif poor == 0:
                    res.append(ans + [candidates[i]])
                    break
                # 剪枝
                if i > 0 and candidates[i] == candidates[i-1] and check[i-1] == 0:
                    continue
                check[i] = 1
                dfs(ans + [candidates[i]], poor, i+1, size)
                check[i] = 0
        candidates.sort()
        res = []
        n = len(candidates)
        check = [0] * n
        dfs([], target, 0, n)
        return res


# 终版
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(ans, target, index, size):
            for i in range(index, size):
                poor = target - candidates[i]
                if poor < 0:
                    break
                elif poor == 0:
                    res.append(ans + [candidates[i]])
                    break
                # 剪枝
                if i > index and candidates[i - 1] == candidates[i]:
                    continue
                dfs(ans + [candidates[i]], poor, i+1, size)
        candidates.sort()
        res = []
        n = len(candidates)
        dfs([], target, 0, n)
        return res


s = Solution()
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8,)



































