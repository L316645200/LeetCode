#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250207_59. 螺旋矩阵 II[medium].py
# @Author  ：Lin
# @Date    ：2025/2/8 17:55
"""59. 螺旋矩阵 II

给你一个正整数n ，生成一个包含 1 到n2所有元素，且元素按顺时针顺序螺旋排列的n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

提示：
	1 <= n <= 20


https://leetcode.cn/problems/spiral-matrix-ii/description/?envType=daily-question&envId=2025-02-07"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        x, y = 0, 0
        cur = 0
        for i in range(n * n):
            matrix[x][y] = i + 1
            dx, dy = directions[cur]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] > 0:
                cur = (cur + 1) % 4
                dx, dy = directions[cur]
            x, y = x + dx, y + dy
        return matrix



s = Solution()
s.generateMatrix(4)
