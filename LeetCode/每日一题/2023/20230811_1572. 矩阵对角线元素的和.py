#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20230811_1572. 矩阵对角线元素的和.py
# @Author: Lin
# @Date  : 2023/8/11 9:23
#
# 给你一个正方形矩阵
# mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
# 示例
# 1：
# 输入：mat = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# 输出：25
# 解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
# 请注意，元素
# mat[1][1] = 5
# 只会被计算一次。
# 示例
# 2：
# 输入：mat = [[1, 1, 1, 1],
#           [1, 1, 1, 1],
#           [1, 1, 1, 1],
#           [1, 1, 1, 1]]
# 输出：8
# 示例
# 3：
# 输入：mat = [[5]]
# 输出：5
# 提示：
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][n-i-1]
        if n % 2 == 1:
            total -= mat[n//2][n//2]
        return total

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n // 2
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        return total - mat[mid][mid] * (n & 1)

s = Solution()
s.diagonalSum(mat = [[1]])