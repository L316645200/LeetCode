#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20241116_3240. 最少翻转次数使二进制矩阵回文 II[medium].py
# @Author  ：Lin
# @Date    ：2024/11/16 9:32


"""给你一个 m x n 的二进制矩阵 grid 。

如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。

你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。

请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 1 的数目可以被 4 整除 。
示例 1：

输入：grid = [[1,0,0],[0,1,0],[0,0,1]]

输出：3

解释：
示例 2：

输入：grid = [[0,1],[0,1],[0,0]]

输出：2

解释：
示例 3：

输入：grid = [[1],[1]]

输出：2

解释：
提示：

m == grid.length
n == grid[i].length
1 <= m * n <= 2 * 105
0 <= grid[i][j] <= 1
"""
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m//2):
            a1, a2 = grid[i], grid[m-1-i]
            for j in range(n//2):
                cnt = a1[j] + a1[n-1-j] + a2[j] + a2[n-1-j]

                res += min(cnt, 4-cnt) #  # 全为 1 或全为 0
        if m % 2 and n % 2:
            # 正中间的数必须是 0
            res += grid[m//2][n//2]

        diff = cnt = 0

        if m % 2:
            # 统计正中间这一排
            a1 = grid[m//2]
            for j in range(n // 2):
                if a1[j] != a1[n-1-j]:
                    diff += 1
                else:
                    cnt += a1[j] * 2

        if n % 2:
            # 统计正中间这一列
            for i in range(m // 2):
                if grid[i][n//2] != grid[m-1-i][n//2]:
                    diff += 1
                else:
                    cnt += grid[i][n//2] * 2
        return res + (diff if diff else cnt % 4)



s = Solution()
s.minFlips(grid = [[0,1,1,0,0,1]])