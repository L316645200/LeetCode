#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天 数组.py
# @Author: Lin
# @Date  : 2021/10/21 16:23
# 566. 重塑矩阵
# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
#
# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
#
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
#
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
#
# 示例 1：
# 输入：mat = [[1,2],[3,4]], r = 1, c = 4
# 输出：[[1,2,3,4]]
# 示例 2：
# 输入：mat = [[1,2],[3,4]], r = 2, c = 4
# 输出：[[1,2],[3,4]]
#  
# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if c * r != m * n:
            return mat
        arr = [[0] * c for _ in range(r)]
        t = 0
        for i in range(r):
            for j in range(c):
                arr[i][j] = mat[t // n][t % n]
                t += 1
        return arr


s = Solution()
s.matrixReshape([[1,2, 3,4]], 2, 2)


# 官解
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]

        return ans


# 118. 杨辉三角
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# 示例 1:
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例 2:
#
# 输入: numRows = 1
# 输出: [[1]]
#  
# 提示:
#
# 1 <= numRows <= 30


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                arr[i].append(1) if j == 0 or j == i else arr[i].append(arr[i-1][j-1] + arr[i-1][j])
        return arr


s = Solution()
res = s.generate(5)
print(res)


# 官解
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

