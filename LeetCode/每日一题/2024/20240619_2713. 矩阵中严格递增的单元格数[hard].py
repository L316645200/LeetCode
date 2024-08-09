#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240619_2713. 矩阵中严格递增的单元格数[hard].py
# @Author  ：Lin
# @Date    ：2024/6/19 16:43


"""给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。
从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。
你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。
请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。
返回一个表示可访问单元格最大数量的整数。
示例 1：
输入：mat = [[3,1],[3,4]]
输出：2
解释：上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。
示例 2：
输入：mat = [[1,1],[1,1]]
输出：1
解释：由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。
示例 3：
输入：mat = [[3,1,6],[-9,5,7]]
输出：4
解释：上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。
提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105"""
from collections import defaultdict
from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = defaultdict(list)
        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                mp[mat[i][j]].append([i, j])

        for _, index in sorted(mp.items(), key=lambda x: x[0]):
            row_mp, col_mp = defaultdict(int), defaultdict(int)
            for i, j in index:
                row_mp[i] = max(row_mp[i], row[i] + 1, col[j] + 1)
                col_mp[j] = max(col_mp[j], row[i] + 1, col[j] + 1)

            for k, v in row_mp.items():
                row[k] = v
            for k, v in col_mp.items():
                col[k] = v
        return max(max(row), max(col))


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        mp = defaultdict(list)
        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                mp[mat[i][j]].append([i, j])

        for _, index in sorted(mp.items(), key=lambda x: x[0]):
            res = [max(row[i], col[j]) + 1 for i, j in index]

            for d, (i, j) in zip(res, index):
                row[i] = max(d, row[i])
                col[j] = max(d, col[j])
        return max(max(row), max(col))


s = Solution()
res = s.maxIncreasingCells(mat =[[-4,8,-3,2,-4,-8,7,5,-2],

                           [-5,5,-7,-2,6,-6,-8,-4,-4]])
print(res)
