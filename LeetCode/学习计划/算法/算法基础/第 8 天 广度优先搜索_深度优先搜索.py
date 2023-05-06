#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 8 天 广度优先搜索_深度优先搜索.py
# @Author: Lin
# @Date  : 2022/7/8 17:58
# 1091. 二进制矩阵中的最短路径
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
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1
# 解题思路
# 典型的BFS最短路径问题，用DFS也可以求解，但是容易超时。
#
# 在二维矩阵中搜索，什么时候用BFS，什么时候用DFS？
# 1.如果只是要找到某一个结果是否存在，那么DFS会更高效。因为DFS会首先把一种可能的情况尝试到底，才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试，在找到一种满足条件的结果的同时，也尝试了很多不必要的路径；
# 2.如果是要找所有可能结果中最短的，那么BFS回更高效。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前，无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时）。而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了，所以这种情况下，BFS更高效。
#
# BFS解法中的visited为什么可以全局使用？
# BFS是在尝试所有的可能路径，哪个最快到达终点，哪个就是最短。那么每一条路径走过的路不同，visited（也就是这条路径上走过的点）也应该不同，那么为什么visited可以全局使用呢？
# 因为我们要找的是最短路径，那么如果在此之前某个点已经在visited中，也就是说有其他路径在小于或等于当前步数的情况下，到达过这个点，证明到达这个点的最短路径已经被找到。那么显然这个点没必要再尝试了，因为即便去尝试了，最终的结果也不会是最短路径了，所以直接放弃这个点即可。
import collections
from typing import List

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        visited = {(0, 0): True}
        level = 1
        deq = deque([(0, 0)])

        while deq:
            for i in range(len(deq)):
                x, y = deq.pop()
                for i, j in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    rows, cols = x + i, y + j
                    if 0 <= rows < n and 0 <= cols < n and grid[rows][cols] == 0 and not visited.get((rows, cols)):
                        if rows == n - 1 and cols == n - 1:
                            return level + 1
                        visited[(rows, cols)] = True
                        deq.appendleft((rows, cols))

            level += 1
        return -1





s = Solution()
s.shortestPathBinaryMatrix([[0]])


# 130. 被围绕的区域
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 示例 1：
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：
# 输入：board = [["X"]]
# 输出：[["X"]]
# 提示：
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        deq = collections.deque()
        visited = {}
        for i in range(m):
            for j in range(n):
                border = False
                s = set()
                if board[i][j] == 'O' and not visited.get((i, j)):
                    deq.append([i, j])
                    visited[(i, j)] = True
                    s.add((i, j))
                    if any([i == 0, i == m - 1, j == 0, j == n - 1]):
                        border = True
                    while deq:
                        sr, sc = deq.popleft()

                        for c, v in [(sr-1, sc), (sr, sc-1), (sr+1, sc), (sr, sc+1)]:

                            if 0 <= c < m and 0 <= v < n and board[c][v] == 'O' and not visited.get((c, v)):
                                deq.append((c, v))
                                visited[(c, v)] = True
                                s.add((c, v))
                                if any([c == 0, c == m - 1, v == 0, v == n - 1]):
                                   border = True
                if border is False:
                    for x, y in s:
                        board[x][y] = 'X'
                else:
                    s.clear()


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"



s = Solution()
s.solve([["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]])


# 797. 所有可能的路径
# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
# 示例 1：
# 输入：graph = [[1,2],[3],[3],[]]
# 输出：[[0,1,3],[0,2,3]]
# 解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
# 示例 2：
# 输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
# 输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 提示：
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i（即不存在自环）
# graph[i] 中的所有元素 互不相同
# 保证输入为 有向无环图（DAG）

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = len(graph) - 1
        res = []

        def dfs(n, arr):
            if n == l:
                res.append(arr[:])
                return
            for g in graph[n]:
                arr.append(g)
                dfs(g, arr)

                arr.pop()
        dfs(0, [0])
        print(res)
        return res

s = Solution()
s.allPathsSourceTarget( [[4,3,1],[3,2,4],[3],[4],[]])
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = len(graph) - 1
        res = []

        def dfs(n, arr):
            if n == l:
                res.append(arr)
                return
            for g in graph[n]:
                dfs(g, arr + [g])

        dfs(0, [0])
        print(res)
        return res
s = Solution()
s.allPathsSourceTarget( [[4,3,1],[3,2,4],[3],[4],[]])































