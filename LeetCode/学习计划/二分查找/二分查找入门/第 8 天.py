#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 8 天.py
# @Author: Lin
# @Date  : 2023/4/17 17:16

# 1351. 统计有序矩阵中的负数
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 grid 中 负数 的数目。
# 示例 1：
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
# 示例 2：
# 输入：grid = [[3,2],[1,0]]
# 输出：0
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0]) - 1
        x = n
        for i in range(m):
            while x > -1 and grid[i][x] < 0:
                x -= 1
            ans += n - x
        return ans


s = Solution()
s.countNegatives(grid = [[3,2],[1,0]])
s.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])


