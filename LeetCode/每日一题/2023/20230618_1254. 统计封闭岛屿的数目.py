#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230618_1254. 统计封闭岛屿的数目.py
# @Author: Lin
# @Date  : 2023/6/28 15:27


# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
# 请返回 封闭岛屿 的数目。
# 示例 1：
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 示例 2：
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 示例 3：
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
# 提示：
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deque = collections.deque()

        def bfs(x, y):
            deque.append((x, y))
            is_close = 1

            while deque:
                x, y = deque.popleft()
                grid[x][y] = -1
                if any([x == 0, x == m - 1, y == 0, y == n - 1]):
                    is_close = 0
                for dx, dy in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                    r = x + dx
                    c = y + dy
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                        deque.append((r, c))
            return is_close

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    res += bfs(i, j)
        return res

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deque = collections.deque()

        res = 0
        for x in range(1, m - 1):
            for y in range(1, n - 1):
                if grid[x][y] == 0:
                    deque.append((x, y))
                    is_close = 1

                    while deque:
                        cx, cy = deque.popleft()
                        grid[cx][cy] = -1
                        if any([cx == 0, cx == m - 1, cy == 0, cy == n - 1]):
                            is_close = 0
                        for dx, dy in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                            r = cx + dx
                            c = cy + dy
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                                deque.append((r, c))
                                grid[r][c] = -1
                    res += is_close
        return res



class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    qu = deque([(i, j)])
                    grid[i][j] = 1
                    closed = True

                    while qu:
                        cx, cy = qu.popleft()
                        if cx == 0 or cy == 0 or cx == m - 1 or cy == n - 1:
                            closed = False
                        for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                                grid[nx][ny] = 1
                                qu.append((nx, ny))
                    if closed:
                        ans += 1

        return ans


s = Solution()
s.closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])


