#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 9 天 递归_回溯.py
# @Author: Lin
# @Date  : 2022/7/19 11:56

# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)

        def backtrack(n, arr):
            res.append(arr)
            for i in range(n, length):
                backtrack(i+1, arr + [nums[i]])
        backtrack(0, [])
        print(res)
        return res


# class Solution(object):
#     def subsets(self, nums):
#         res, path = [], []
#         self.dfs(nums, 0, res, path)
#         return res
#
#     def dfs(self, nums, index, res, path):
#         res.append(copy.deepcopy(path))
#         for i in range(index, len(nums)):
#             path.append(nums[i])
#             self.dfs(nums, i + 1, res, path)
#             path.pop()


s = Solution()
s.subsets(nums = [1,2,3])
res = []
path = []

# def backtrack(未探索区域, res, path):
#     if path 满足条件:
#         res.add(path) # 深度拷贝
#         # return  # 如果不用继续搜索需要 return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()


# 90. 子集 II
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 示例 1：
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         res, path = [], []
#         nums.sort()
#         self.dfs(nums, 0, res, path)
#         return res
#
#     def dfs(self, nums, index, res, path):
#         res.append(copy.deepcopy(path))
#         for i in range(index, len(nums)):
#             if i > index and nums[i] == nums[i - 1]:
#                 continue
#             path.append(nums[i])
#             self.dfs(nums, i + 1, res, path)
#             path.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        def backtrack(n, arr):
            if arr not in res:
                res.append(arr)
            for i in range(n, length):
                backtrack(i+1, arr + [nums[i]])
        backtrack(0, [])
        print(res)
        return res


s = Solution()
s.subsetsWithDup(nums =[4,4,4,1,4])


