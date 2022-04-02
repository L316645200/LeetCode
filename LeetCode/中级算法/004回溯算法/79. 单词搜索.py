#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 79. 单词搜索.py
# @Author: Lin
# @Date  : 2022/2/24 15:17

# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
# 示例 3：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
#  
# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#  
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
import collections
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word) - 1
        temp = [[0 for _ in range(n)] for __ in range(m)]

        def hasback(index, i, j):
            r = 0
            temp[i][j] = 1
            for p, q in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if (0 <= p < m) and (0 <= q < n) and temp[p][q] == 0 and board[p][q] == word[index]:
                    if index == l:
                        return 1
                    r += hasback(index + 1, p, q)

            temp[i][j] = 0
            return r

        r = 0
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if l == 0:
                        r += 1
                        break
                    r += hasback(1, i, j)

        return r >= 1


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word) - 1
        temp = set()

        def hasback(index, i, j):
            r = 0
            temp.add((i, j))
            for p, q in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if (0 <= p < m) and (0 <= q < n) and (p, q) in temp and board[p][q] == word[index]:
                    if index == l:
                        return 1
                    r += hasback(index + 1, p, q)
            temp.remove((i, j))
            return r

        r = 0
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if l == 0:
                        r += 1
                        break
                    r += hasback(1, i, j)

        return r >= 1


s = Solution()
r = s.exist([["a", "a"]], "a")
print(r)