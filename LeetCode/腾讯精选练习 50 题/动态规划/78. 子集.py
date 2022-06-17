#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 78. 子集.py
# @Author: Lin
# @Date  : 2022/5/25 10:08

# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]子集
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
from typing import List


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
s.subsets([1,2,3])