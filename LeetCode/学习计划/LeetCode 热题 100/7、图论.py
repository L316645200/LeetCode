#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：7、图论.py
# @Author  ：Lin
# @Date    ：2024/6/4 17:17

"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""
import collections
from collections import deque
from typing import List


# 广度
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    deq = deque([(i, j)])
                    grid[i][j] = '0'
                    while deq:
                        x, y = deq.popleft()
                        for dir_x, dir_y in direction:
                            p, q = x + dir_x, y + dir_y
                            if 0 <= p < m and 0 <= q < n and grid[p][q] == '1':
                                deq.append((p, q))
                                grid[p][q] = '0'
                    res += 1
        return res

# 深度
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, direction)
                    res += 1
        return res

    def dfs(self, i, j, grid, direction) -> int:
        grid[i][j] = '0'
        m, n = len(grid), len(grid[0])

        for dir_x, dir_y in direction:
            p, q = i + dir_x, j + dir_y
            if 0 <= p < m and 0 <= q < n and grid[p][q] == '1':
                self.dfs(p, q, grid, direction)


# s = Solution()
# s.numIslands(grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ])


"""994. 腐烂的橘子
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deq = []
        res, fresh_num = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    deq.append((i, j))
                elif grid[i][j] == 1:
                    fresh_num += 1 # 总的新鲜橘子数

        while deq:
            arr = []
            for i, j in deq:
                for x, y in [(i + 1, j), (i, j + 1), (i - 1,  j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        arr.append((x, y))
                        fresh_num -= 1  # 新鲜的橘子腐烂
                        grid[x][y] = 2
            deq = arr.copy()
            if arr:
                res += 1
        # 不存在新鲜的橘子了
        return res if fresh_num == 0 else -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        def neighbors(i, j):
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))
        if any(1 in row for row in grid):
            return -1
        return d
# s = Solution()
# s.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]])


"""207. 课程表
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
提示：
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同
"""


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         edges = collections.defaultdict(list)
#         visited = [0] * numCourses
#         for u, v in prerequisites:
#             edges[u].append(v)
#         print(edges)
#
#         def dfs(x: int):
#             mark = True
#             if visited[x] == 1:
#                 mark = False
#             elif visited[x] == 0:
#                 visited[x] = 1
#                 for y in edges[x]:
#                     if not dfs(y):
#                         mark = False
#             visited[x] = 2
#             return mark
#
#         for i in range(numCourses):
#             if i in edges and not dfs(i):
#                 return False
#         return True


class Solution:
    # 深度优先搜索
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        for u, v in prerequisites:
            edges[u].append(v)

        def dfs(u: int):
            mark = True
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    if not dfs(v):
                        mark = False
                elif visited[v] == 1:
                    mark = False
            visited[u] = 2
            return mark

        for i in range(numCourses):
            if i in edges and not dfs(i):
                return False
        return True



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for u, v in prerequisites:
            edges[v].append(u)
            indeg[u] += 1

        deq = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        cnt = 0
        while deq:
            u = deq.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    deq.append(v)
            cnt += 1

        return cnt == numCourses


s = Solution()
s.canFinish(numCourses = 2, prerequisites = [[1,0]])
