#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 5 天 数组.py
# @Author: Lin
# @Date  : 2021/10/21 17:13
# 36. 有效的数独
#
# 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
#
# 示例 1：
#
# 输入：board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
# 示例 2：
#
# 输入：board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
# 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
#  
# 提示：
#
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
from typing import List


# 不知道哪里抄的
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for n in range(9)]
        columns = [{} for n in range(9)]
        box = [{} for n in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][board[i][j]] = rows[i].get(board[i][j], 0) + 1
                    columns[j][board[i][j]] = columns[j].get(board[i][j], 0) + 1

                    box[box_index][board[i][j]] = box[box_index].get(board[i][j], 0) + 1

                    if rows[i][board[i][j]] > 1 or columns[j][board[i][j]] > 1 or box[box_index][board[i][j]] > 1:
                        return False
        return True


# 自己写的
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: [] for i in range(9)}
        column = {i: [] for i in range(9)}
        block = {i: [] for i in range(9)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                n = i // 3 * 3 + j // 3
                if num != '.':
                    if num not in row[i] and num not in column[j] and num not in block[n]:
                        row[i].append(num)
                        column[j].append(num)
                        block[n].append(num)
                    else:
                        return False
        return True


# 73. 矩阵置零
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 进阶：
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#  
# 示例 1：
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：
#
#
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 提示：
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for r in row:
            for _ in range(n):
                matrix[r][_] = 0
        for c in column:
            for _ in range(m):
                matrix[_][c] = 0

s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


# 官解1 空间复杂度降低
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

# 官解2 空间复杂度降低
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False

        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0



