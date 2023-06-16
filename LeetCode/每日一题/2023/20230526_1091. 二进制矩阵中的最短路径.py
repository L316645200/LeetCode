#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230526_1091. 二进制矩阵中的最短路径.py
# @Author: Lin
# @Date  : 2023/5/26 10:31

# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。
# 示例 1：
# 输入：grid = [[0,1],[1,0]]
# 输出：2
# 示例 2：
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
# 示例 3：
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        if n == 1:
            return 1
        visited = {(0, 0): 1}
        deq = deque([(0, 0)])
        gl = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]
        ans = 1
        while deq:
            ans += 1
            for i in range(len(deq)):
                x, y = deq.pop()
                for i, j in gl:
                    rows, cols = x + i, y + j
                    if 0 <= rows < n and 0 <= cols < n and not visited.get((rows, cols)) and grid[rows][cols] == 0:
                        if rows == n - 1 and cols == n - 1:
                            return ans
                        visited[(rows, cols)] = 1
                        deq.appendleft((rows, cols))

        return -1
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        if n == 1:
            return 1
        dist = [[float('inf')] * n for i in range(n)]
        dist[0][0] = 1
        deq = deque([(0, 0)])
        while deq:
            for i in range(len(deq)):
                x, y = deq.pop()
                if x == n - 1 and y == n - 1:
                    return dist[x][y]
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= x + dx < n and 0 <= y + dy < n and grid[x + dx][y + dy] == 0 and dist[x + dx][y + dy] > dist[x][y] + 1:
                            dist[x + dx][y + dy] = dist[x][y] + 1
                            deq.appendleft((x + dx,  y + dy))
        return -1



s = Solution()
# s.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]])
# r = s.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]])
r = s.shortestPathBinaryMatrix(grid = [[0,1],[1,0]])
print(r)
# s.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]])
