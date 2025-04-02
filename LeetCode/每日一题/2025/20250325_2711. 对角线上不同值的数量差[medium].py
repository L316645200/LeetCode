#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/25 12:39
# @Author  : Lin
# @File    : 20250325_2711. 对角线上不同值的数量差[medium].py
"""给你一个下标从 0 开始、大小为 m x n 的二维矩阵 grid ，请你求解大小同样为 m x n 的答案矩阵 answer 。

矩阵 answer 中每个单元格 (r, c) 的值可以按下述方式进行计算：

令 topLeft[r][c] 为矩阵 grid 中单元格 (r, c) 左上角对角线上 不同值 的数量。
令 bottomRight[r][c] 为矩阵 grid 中单元格 (r, c) 右下角对角线上 不同值 的数量。
然后 answer[r][c] = |topLeft[r][c] - bottomRight[r][c]| 。

返回矩阵 answer 。

矩阵对角线 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。

如果单元格 (r1, c1) 和单元格 (r, c) 属于同一条对角线且 r1 < r ，则单元格 (r1, c1) 属于单元格 (r, c) 的左上对角线。类似地，可以定义右下对角线。



示例 1：


输入：grid = [[1,2,3],[3,1,5],[3,2,1]]
输出：[[1,1,0],[1,0,1],[0,1,1]]
解释：第 1 个图表示最初的矩阵 grid 。
第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。
第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。
第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。
- 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。
- 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。
- 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。
其他单元格的对应答案也可以按照这样的流程进行计算。
示例 2：

输入：grid = [[1]]
输出：[[0]]
解释：- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。


提示：

m == grid.length
n == grid[i].length
1 <= m, n, grid[i][j] <= 50"""
from collections import defaultdict
from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            suf = defaultdict(int)
            pre = defaultdict(int)
            for j in range(min(m-i, n)):
                suf[grid[i + j][j]] += 1
            for j in range(min(m-i, n)):
                suf[grid[i + j][j]] -= 1
                if suf[grid[i + j][j]] == 0:
                    del suf[grid[i + j][j]]
                ans[i + j][j] = abs(len(pre) - len(suf))
                pre[grid[i + j][j]] += 1

        for j in range(1, n):
            suf = defaultdict(int)
            pre = defaultdict(int)
            for i in range(min(n-j, m)):
                suf[grid[i][i+j]] += 1
            for i in range(min(n-j, m)):
                suf[grid[i][i+j]] -= 1
                if suf[grid[i][i+j]] == 0:
                    del suf[grid[i][i+j]]
                ans[i][i+j] = abs(len(pre) - len(suf))
                pre[grid[i][i+j]] += 1
        return ans

s = Solution()
# s.differenceOfDistinctValues(grid = [[1,2,3],[3,1,5],[3,2,1]])
s.differenceOfDistinctValues([[6,28,37,34,12,30,43,35,6],[21,47,38,14,31,49,11,14,49],[6,12,35,17,17,2,45,27,43],[34,41,30,28,45,24,50,20,4]])