#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240513_994. 腐烂的橘子.py
# @Author  ：Lin
# @Date    ：2024/5/13 15:53


"""在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

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
grid[i][j] 仅为 0、1 或 2"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deq = []
        ans, fresh_num = 0, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    deq.append((i, j))
                elif grid[i][j] == 1:
                    fresh_num += 1

        while deq:
            arr = []
            for i, j in deq:
                for p, q in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        grid[p][q] = 2
                        fresh_num -= 1
                        arr.append((p, q))
            if len(arr):
                ans += 1
            deq = arr.copy()
        return ans if fresh_num == 0 else -1


s = Solution()
s.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]])







