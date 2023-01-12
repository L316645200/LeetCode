#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 3 天 数组.py
# @Author: Lin
# @Date  : 2022/10/13 16:26
# 119. 杨辉三角 II
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
# 示例 2:
# 输入: rowIndex = 0
# 输出: [1]
# 示例 3:
# 输入: rowIndex = 1
# 输出: [1,1]
# 提示:
# 0 <= rowIndex <= 33
# 进阶：
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i - 1, 0, -1):
                dp[j] = dp[j-1] + dp[j]
        return dp

s = Solution()
s.getRow(3)

# 48. 旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
# 示例 2：
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 提示：
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        left, right = 0, n
        while left <= right:
            for i in range(left, right):
                matrix[i][n-left], matrix[n-left][n-i], matrix[n-i][left], matrix[left][i] \
                    = matrix[left][i], matrix[i][n-left], matrix[n-left][n-i], matrix[n-i][left]
            left += 1
            right -= 1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix) - 1
        for i in range(l):
            for j in range(i, l-i):
                target = matrix[i][j]
                matrix[i][j] = matrix[l-j][i]
                matrix[l-j][i] = matrix[l-i][l-j]
                matrix[l-i][l-j] = matrix[j][l-i]
                matrix[j][l-i] = target
        print(matrix)

s = Solution()
s.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
s.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])