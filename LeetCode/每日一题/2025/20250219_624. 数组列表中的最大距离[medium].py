#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250219_624. 数组列表中的最大距离[medium].py
# @Author  ：Lin
# @Date    ：2025/2/19 9:46
"""624. 数组列表中的最大距离

给定m个数组，每个数组都已经按照升序排好序了。
现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数a和b之间的距离定义为它们差的绝对值|a-b|。
返回最大距离。

示例 1：
输入：[[1,2,3],[4,5],[1,2,3]]
输出：4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。

示例 2：
输入：arrays = [[1],[1]]
输出：0

提示：
	m == arrays.length
	2 <= m <= 10^5
	1 <= arrays[i].length <= 500
	-10^4 <= arrays[i][j] <= 10^4
	arrays[i]以升序排序。
	所有数组中最多有10^5 个整数。


https://leetcode.cn/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2025-02-19"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi, mx = arrays[0][0], arrays[0][-1]
        res = 0
        for l in arrays[1:]:
            res = max(res, l[-1] - mi, mx - l[0])
            mi = min(mi, l[0])
            mx = max(mx, l[-1])
        return res


s = Solution()
r = s.maxDistance([[1,4],[0,5]])
print(r)
