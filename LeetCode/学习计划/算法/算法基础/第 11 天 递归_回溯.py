# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @File  : 第 11 天 递归_回溯.py
# # @Author: Lin
# # @Date  : 2022/8/12 15:28
#
# 17. 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：
# 输入：digits = ""
# 输出：[]
# 示例 3：
# 输入：digits = "2"
# 输出：["a","b","c"]
# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
#
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_to_letter = {"1": "", "2": "abc", "3": "def",
                            "4": "ghi", "5": "jkl", "6": "mno",
                            "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        ans = []
        def dfs(s, index):
            if len(s) == n:
                ans.append(s)
                return
            for letter in digits_to_letter[digits[index]]:
                dfs(s + letter, index+1)
        dfs("", 0)
        return ans

s = Solution()
s.letterCombinations("23")

# 22. 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
# 输入：n = 1
# 输出：["()"]
# 提示：
# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s, left, right):
            if right > left or left > n:
                return
            if len(s) == 2 * n:
                ans.append(s)
                return
            dfs(s + "(", left+1, right)
            dfs(s + ")", left, right+1)

        dfs("", 0, 0)
        return ans

s = Solution()
s.generateParenthesis(2)

# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
# 示例 3：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#  
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word) - 1
        tmp = [[0] * n for _ in range(m)]
        def bfs(i, j, index):
            r = 0
            tmp[i][j] = 1
            for p, q in ([(i+1, j), (i, j+1), (i-1, j), (i, j-1)]):
                if 0 <= p < m and 0 <= q < n and tmp[p][q] == 0 and word[index] == board[p][q]:
                    if index == l:
                        return 1
                    r += bfs(p, q, index+1)
            tmp[i][j] = 0
            return r
        r = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if l == 0:
                        return True
                    r += bfs(i, j, 1)
                    if r >= 1:
                        return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word) - 1
        tmp = [[0] * n for _ in range(m)]
        def bfs(i, j, index):
            if board[i][j] != word[index]:
                return False
            if l == index:
                return True
            tmp[i][j] = 1
            for p, q in ([(i+1, j), (i, j+1), (i-1, j), (i, j-1)]):
                if 0 <= p < m and 0 <= q < n and tmp[p][q] == 0:
                    if bfs(p, q, index+1):
                        return True
            tmp[i][j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if bfs(i, j, 0):
                    return True
        return False

s = Solution()
r = s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print(r)



























