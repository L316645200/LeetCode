#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 6 天 广度优先搜索and深度优先搜索.py
# @Author: Lin
# @Date  : 2022/6/17 11:02
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
# 示例 1：
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # arr = [[0] * n for _ in range(m)]
        ans = 0
        deq = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    deq.append((i, j))
                    while deq:
                        sr, sc = deq.popleft()
                        for c, v in [(sr-1, sc), (sr, sc-1), (sr+1, sc), (sr, sc+1)]:
                            if 0 <= c < m and 0 <= v < n and grid[c][v] == '1':
                                deq.append((c, v))
                                grid[c][v] = '0'
        return ans


s = Solution()
s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

# 547. 省份数量
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
# 返回矩阵中 省份 的数量。
# 示例 1：
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 示例 2：
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
# 提示：
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, ans = len(isConnected), 0
        seen = set()
        deq = collections.deque()
        for i in range(n):
            if i not in seen:
                ans += 1
                deq.append(i)
                while deq:
                    row = deq.popleft()
                    for j in range(n):
                        if j not in seen and isConnected[row][j] == 1:
                            deq.append(j)
                            seen.add(j)
        return ans
s = Solution()
s.findCircleNum(isConnected =[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])