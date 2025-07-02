#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/5/23 17:54
# @Author  : Lin
# @File    : 20250520_3355. 零数组变换 I[mid].py
"""3355. 零数组变换 I
给定一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [li, ri]。
对于每个查询 queries[i]：
在 nums 的下标范围 [li, ri] 内选择一个下标 子集。
将选中的每个下标对应的元素值减 1。
零数组 是指所有元素都等于 0 的数组。
如果在按顺序处理所有查询后，可以将 nums 转换为 零数组 ，则返回 true，否则返回 false。
示例 1：
输入： nums = [1,0,1], queries = [[0,2]]
输出： true
解释：
对于 i = 0：
选择下标子集 [0, 2] 并将这些下标处的值减 1。
数组将变为 [0, 0, 0]，这是一个零数组。
示例 2：
输入： nums = [4,3,2,1], queries = [[1,3],[0,2]]
输出： false
解释：
对于 i = 0：
选择下标子集 [1, 2, 3] 并将这些下标处的值减 1。
数组将变为 [4, 2, 1, 0]。
对于 i = 1：
选择下标子集 [0, 1, 2] 并将这些下标处的值减 1。
数组将变为 [3, 1, 0, 0]，这不是一个零数组。
提示：
1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length
"""

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for i, j in queries:
            diff[i] += 1
            diff[j+1] -= 1

        sum_d = 0
        for x, d in zip(nums, diff):
            sum_d += d
            if x > sum_d:
                return False
        return True

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for i, j in queries:
            diff[i] += 1
            diff[j+1] -= 1

        for x, sum_d in zip(nums, accumulate(diff)):
            if x > sum_d:
                return False
        return True