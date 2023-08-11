#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230810_1289. 下降路径最小和 II.py
# @Author: Lin
# @Date  : 2023/8/10 9:55

# 给你一个
# n
# x
# n
# 整数矩阵
# grid ，请你返回
# 非零偏移下降路径
# 数字和的最小值。
#
# 非零偏移下降路径
# 定义为：从
# grid
# 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
# 示例
# 1：
# 输入：grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1, 5, 9], [1, 5, 7], [1, 6, 7], [1, 6, 8],
# [2, 4, 8], [2, 4, 9], [2, 6, 7], [2, 6, 8],
# [3, 4, 8], [3, 4, 9], [3, 5, 7], [3, 5, 9]
# 下降路径中数字和最小的是[1, 5, 7] ，所以答案是
# 13 。
# 示例
# 2：
# 输入：grid = [[7]]
# 输出：7
# 提示：
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        first, second = float('inf'), float('inf')

        for i in range(n):

            if i > 0:
                for j in range(n):
                    if grid[i-1][j] == first:
                        grid[i][j] += second
                    else:
                        grid[i][j] += first
            first, second = float('inf'), float('inf')

            for j in range(n):
                if first > grid[i][j]:
                    first, second = grid[i][j], first
                elif second > grid[i][j]:
                    second = grid[i][j]
        return first


s = Solution()
s.minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]])