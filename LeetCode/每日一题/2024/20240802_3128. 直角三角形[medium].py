#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20240802_3128. 直角三角形[medium].py
# @Author  ：Lin
# @Date    ：2024/8/2 17:26


"""给你一个二维 boolean 矩阵 grid 。

请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。

注意：

如果 grid 中 3 个元素满足：一个元素与另一个元素在 同一行，同时与第三个元素在 同一列 ，那么这 3 个元素称为一个 直角三角形 。这 3 个元素互相之间不需要相邻。


示例 1：

0	1	0
0	1	1
0	1	0
0	1	0
0	1	1
0	1	0
输入：grid = [[0,1,0],[0,1,1],[0,1,0]]

输出：2

解释：

有 2 个直角三角形。

示例 2：

1	0	0	0
0	1	0	1
1	0	0	0
输入：grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]

输出：0

解释：

没有直角三角形。

示例 3：

1	0	1
1	0	0
1	0	0
1	0	1
1	0	0
1	0	0
输入：grid = [[1,0,1],[1,0,0],[1,0,0]]

输出：2

解释：

有两个直角三角形。



提示：

1 <= grid.length <= 1000
1 <= grid[i].length <= 1000
0 <= grid[i][j] <= 1"""
from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [0] * m, [0] * n
        # 遍历得出矩阵grid每行每列各有多少个1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        res = 0
        # 遍历矩阵grid，以当前点为直角三角形的直角点，则可以构建的直角三角形数目为(row[i] - 1) * (col[j] - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (row[i] - 1) * (col[j] - 1)
        return res




s = Solution()
s.numberOfRightTriangles(grid = [[0,1,0],[0,1,1],[0,1,0]])

















