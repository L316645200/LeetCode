#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：8、回溯.py
# @Author  ：Lin
# @Date    ：2024/6/18 17:33
import itertools
from functools import cache
from typing import List
"""46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]
输出：[[1]]
提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同"""
# 深度优先遍历

#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 标记数组
        is_visited = [False] * len(nums)
        ans = []
        #
        def dfs(arr, depth):
            # 深度和数组长度相同，就结束
            if depth == len(nums):
                ans.append(arr)
                return
            for i in range(len(nums)):
                # 没访问过的
                if not is_visited[i]:
                    is_visited[i] = True
                    dfs(arr + [nums[i]], depth + 1)
                    is_visited[i] = False

        dfs([], 0)
        return ans


# 方法一：回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(first=0):
            if first == len(nums):
               ans.append(nums[:])

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        backtrack()
        return ans


s = Solution()
s.permute([1,2,3])


"""78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""

# 每次选或不选当前值
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         path = []
#         n = len(nums)
#         def dfs(i: int):
#             if i == n:
#                 ans.append(path.copy())
#                 return
#             dfs(i + 1)
#             path.append(nums[i])
#             dfs(i + 1)
#             path.pop()
#         dfs(0)
#         return ans

# 遍历递归
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        n = len(nums)
        def dfs(arr: list, j: int):
            ans.append(arr)
            for i in range(j, n):
                dfs(arr + [nums[i]], i + 1)
        dfs([], 0)
        return ans


s = Solution()
s.subsets(nums = [1,2,3])



"""17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：
输入：digits = ""
输出：[]
示例 3：
输入：digits = "2"
输出：["a","b","c"]
提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        n = len(digits)
        if n == 0:
            return ans
        mp = {'2':'abc', '3':'def', '4':'ghi',
              '5':'jkl', '6':'mno', '7':'pqrs',
              '8':'tuv', '9':'wxyz'}

        def dfs(arr, i):
            if i == n:
                ans.append(''.join(arr))
                return
            for d in mp[digits[i]]:
                dfs(arr + [d], i + 1)

        dfs([], 0)
        return ans


s = Solution()
s.letterCombinations(digits = "23")



"""39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：
输入: candidates = [2], target = 1
输出: []
提示：
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def dfs(arr, j, diff):
            if diff == 0:
                ans.append(arr)
                return
            elif diff < 0:
                return
            for i in range(j, n):
                dfs(arr + [candidates[i]], i, diff - candidates[i])

        dfs([], 0, target)
        return ans

# 选或不选：类似完全背包

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def dfs(arr, i, diff):
            if diff == 0:
                ans.append(arr)
                return
            elif diff < 0:
                return

            dfs(arr + [candidates[i]], i, diff - candidates[i])
            if i < n - 1:
                dfs(arr, i + 1, diff)

        dfs([], 0, target)
        return ans


"""22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
提示：
1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = n, 0
        ans = []
        def dfs(arr, left, right):
            if left == right == 0:
                ans.append(''.join(arr))
                return
            if left > 0:
                dfs(arr + ['('], left - 1, right + 1)
            if right > 0:
                dfs(arr + [')'], left, right - 1)

        dfs([], left, right)
        return ans


s = Solution()
s.generateParenthesis(n = 3)


"""79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
提示：
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        is_visited = [[False for _ in range(n)] for _ in range(m)]
        res = False

        def bfs(i, j, c):
            nonlocal res
            if c == len(word):
                res = True
                return
            for ix, jx in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ix < m and 0 <= jx < n and not is_visited[ix][jx] and board[ix][jx] == word[c]:
                    is_visited[ix][jx] = True
                    bfs(ix, jx, c + 1)
                    is_visited[ix][jx] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    is_visited[i][j] = True
                    bfs(i, j, 1)
                    is_visited[i][j] = False
        return res


"""131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 
回文串
 。返回 s 所有可能的分割方案。
示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：
输入：s = "a"
输出：[["a"]]
提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(arr, i):
            if i == n:
                ans.append(arr)
                return
            for j in range(i, n):
                if is_palindrome(i, j):
                    dfs(arr + [s[i:j+1]], j + 1)

        ans = []
        n = len(s)
        dfs([], 0)
        return ans


"""51. N 皇后
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：
输入：n = 1
输出：[["Q"]]
提示：
1 <= n <= 9
"""

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         s = [[i,0] for i in range(n)]
#         t = [i for i in range(n)]
#         pu = list(itertools.permutations(t))
#         print(pu)
#         print(s)
#         print(t)
#         r = []
#         for l in pu:
#             for i in range(n):
#                 s[i][1] = l[i]
#                 t[i] = s[i][0] + s[i][1]
#             # print()
#             # print(s)
#             # print(t)
#
#             if len(set(t)) == n:
#                 for i in range(n):
#                     t[i] = t[i] - 2*i
#                 if len(set(t)) == n:
#                     res = []
#                     for i in s:
#                         st = '.' * i[1] + 'Q' + '.' * (n-i[1]-1)
#                         res.append(st)
#                     r.append(res)
#         return r


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        is_attacked = [[0] * n for _ in range(n)]
        board = [['.'] * n for _ in range(n)]

        def attack_range(i, j, k):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x, y, stride = i, j, 1
                    if not (dx == 0 and dy == 0):
                        while 0 <= i + stride * dx < n and 0 <= j + stride * dy < n:
                            is_attacked[i + stride * dx][j + stride * dy] += k
                            stride += 1

        ans = []

        def dfs(x):
            if x == n:
                ans.append([''.join(b) for b in board])
                return
            for i in range(n):
                if is_attacked[x][i] == 0:
                    board[x][i] = 'Q'
                    attack_range(x, i, 1)
                    dfs(x+1)
                    board[x][i] = '.'
                    attack_range(x, i, -1)

        dfs(0)
        return ans


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        positive_angles = [False] * (2 * n)
        negative_angles = [False] * (2 * n)
        board = [['.'] * n for _ in range(n)]
        ans = []

        def dfs(x):
            if x == n:
                ans.append([''.join(row) for row in board])
                return
            for i in range(n):
                if not cols[i] and not positive_angles[i-x+n-1] and not negative_angles[i+x]:
                    board[x][i] = 'Q'
                    cols[i] = positive_angles[i-x+n-1] = negative_angles[i + x] = True
                    dfs(x+1)
                    board[x][i] = '.'
                    cols[i] = positive_angles[i-x+n-1] = negative_angles[i + x] = False
        dfs(0)
        return ans


# 0 <= i + j <= 2 * n - 2
# -n + 1  <=  i - j <= n - 1


s = Solution()
s.solveNQueens(4)



































































