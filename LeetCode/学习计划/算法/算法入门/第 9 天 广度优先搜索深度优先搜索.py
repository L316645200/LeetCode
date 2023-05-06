#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 7 天 广度优先搜索深度优先搜索.py
# @Author: Lin
# @Date  : 2021/7/31 17:36
# 542. 01 矩阵
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#
# 示例 1：
#
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
# 示例 2：
#
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#  
# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0 
import collections
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)

        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:

            i, j = q.popleft()

            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist


# mat = [[0,0,0],[0,1,0],[1,1,1]]
# s = Solution()
# s.updateMatrix(mat)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = [(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 2]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(arr)
        ma = 0

        # 广度优先搜索
        while q:
            i, j, ma = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, ma + 1))
        r = -1 if [1 for i in range(m) for j in range(n) if grid[i][j] == 1] else 0
        return r or ma
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
s = Solution()
s.orangesRotting(grid)