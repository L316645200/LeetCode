#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 78. 子集.py
# @Author: Lin
# @Date  : 2022/2/23 17:07
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
from itertools import combinations
from typing import List


# 库函数 自己写的
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        return [list(j) for i in range(len(nums) + 1) for j in combinations(nums, i)]


# 迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            print(i, [num for num in res])

            res = res + [[i] + num for num in res]
        return res

arr =[1, 2, 3]
s = Solution()
s.subsets(arr)


# 自己写的
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def hastack(arr, index):
            print(arr, index)
            res.append(arr)
            for i in range(index, n):
                hastack(arr + [nums[i]], i + 1)
        hastack([], 0)
        return res
s = Solution()
# s.subsets([1, 2, 3])

def subsequences(arr):
    sub = []
    end = 1 << (size := len(arr))  # 1 << x == 2 ** x
    print(end)
    for index in range(end):
        array = []
        for j in range(size):
            print(index, j, index >> j)
            if (index >> j) % 2:
                array.append(arr[j])
            # print(index, j, index >> j, array)

        sub.append(array)
    return sub


arr =[1, 2, 3]
subsequences(arr)

