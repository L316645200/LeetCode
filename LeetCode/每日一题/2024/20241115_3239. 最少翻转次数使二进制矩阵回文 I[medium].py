#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241115_3239. 最少翻转次数使二进制矩阵回文 I[medium].py
# @Author  ：Lin
# @Date    ：2024/11/15 10:16
"""给你一个 m x n 的二进制矩阵 grid 。
如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
请你返回 最少 翻转次数，使得矩阵 要么 所有行是 回文的 ，要么所有列是 回文的 。
示例 1：
输入：grid = [[1,0,0],[0,0,0],[0,0,1]]
输出：2
解释：
将高亮的格子翻转，得到所有行都是回文的。
示例 2：
输入：grid = [[0,1],[0,1],[0,0]]
输出：1
解释：
将高亮的格子翻转，得到所有列都是回文的。
示例 3：
输入：grid = [[1],[0]]
输出：0
解释：
所有行已经是回文的。
提示：
m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1"""
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt1 = cnt2 = 0
        for i in range(m):
            left, right = 0, n-1
            while left < right:
                if grid[i][left] != grid[i][right]:
                    cnt1 += 1
                left += 1
                right -= 1

        for j in range(n):
            left, right = 0, m-1
            while left < right:
                if grid[left][j] != grid[right][j]:
                    cnt2 += 1
                left += 1
                right -= 1
        return min(cnt1, cnt2)

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def f(m: int, n: int, d: int) -> int:
            cnt = 0
            for i in range(m):
                left, right = 0, n - 1
                while left < right:
                    if d == 0:
                        if grid[i][left] != grid[i][right]:
                            cnt += 1
                    else:
                        if grid[left][i] != grid[right][i]:
                            cnt += 1
                    left += 1
                    right -= 1
            return cnt
        return min(f(m, n, 0), f(n, m, 1))


s = Solution()
s.minFlips(grid = [[0,1],[0,1],[0,0]])