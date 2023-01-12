#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20220905_1582. 二进制矩阵中的特殊位置.py
# @Author: Lin
# @Date  : 2022/9/5 10:52

# 给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。
# 特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。
# 示例 1：
# 输入：mat = [[1,0,0],
#             [0,0,1],
#             [1,0,0]]
# 输出：1
# 解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0
# 示例 2：
# 输入：mat = [[1,0,0],
#             [0,1,0],
#             [0,0,1]]
# 输出：3
# 解释：(0,0), (1,1) 和 (2,2) 都是特殊位置
# 示例 3：
# 输入：mat = [[0,0,0,1],
#             [1,0,0,0],
#             [0,1,1,0],
#             [0,0,0,0]]
# 输出：2
# 示例 4：
# 输入：mat = [[0,0,0,0,0],
#             [1,0,0,0,0],
#             [0,1,0,0,0],
#             [0,0,1,0,0],
#             [0,0,0,1,1]]
# 输出：3
# 提示：
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] 是 0 或 1
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # mark0 = [0 for _ in range(m)]
        # mark1 = [0 for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 1:
        #             mark0[i] += 1
        #             mark1[j] += 1
        mark0 = [sum(row) for row in mat]
        mark1 = [sum(col) for col in zip(*mat)]
        for i, v in enumerate(mark0):
            if v >= 2:
                for j in range(n):
                    mat[i][j] = 0
        for j, v in enumerate(mark1):
            if v >= 2:
                for i in range(m):
                    mat[i][j] = 0
                    print(mat)
        print(mat)

        return sum([sum(_) for _ in mat])

# 上下两个函数原理是相同的

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)]
        print(rows_sum)
        print(cols_sum)
        res = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                    res += 1
        return res

s = Solution()
r = s.numSpecial(mat =
[[1,0,0],
 [0,0,1],
 [1,0,0]])
print(r)

