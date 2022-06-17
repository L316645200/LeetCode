#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 54. 螺旋矩阵.py
# @Author: Lin
# @Date  : 2022/5/2 15:21
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length, count = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        mark = [[0]*count for _ in range(length)]
        mark[0][0] = 1
        total = length * count
        arr = [matrix[0][0]]
        current = [0, 0]
        n, rem = 0, 0

        for i in range(total-1):
            if not (0 <= current[0] + directions[rem][0] < length) or not (0 <= current[1] + directions[rem][1] < count):
                n += 1
            else:
                t = [current[0] + directions[rem][0], current[1] + directions[rem][1]]
                if mark[t[0]][t[1]] == 1:
                    n += 1
            rem = n % 4

            current = [current[0] + directions[rem][0], current[1] + directions[rem][1]]
            mark[current[0]][current[1]] = 1
            arr.append(matrix[current[0]][current[1]])
        print(arr)
        return arr




s = Solution()
s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])