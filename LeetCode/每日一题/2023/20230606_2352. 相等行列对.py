#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230606_2352. 相等行列对.py
# @Author: Lin
# @Date  : 2023/6/9 11:55

# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
# 示例 1：
# 输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
# 输出：1
# 解释：存在一对相等行列对：
# - (第 2 行，第 1 列)：[2,7,7]
# 示例 2：
# 输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# 输出：3
# 解释：存在三对相等行列对：
# - (第 0 行，第 0 列)：[3,1,2,2]
# - (第 2 行, 第 2 列)：[2,4,2,2]
# - (第 3 行, 第 2 列)：[2,4,2,2]
# 提示：
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105
from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column = Counter()
        n = len(grid)
        for i in range(n):
            column[tuple(grid[i])] += 1

        return sum([column[tuple([grid[j][i] for j in range(n)])] for i in range(n) ])


s = Solution()
s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])

