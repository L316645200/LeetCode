#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2、矩阵.py
# @Author: Lin
# @Date  : 2023/7/1 15:25


# 62. 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？
# 示例 1：
# 输入：m = 3, n = 7
# 输出：28
# 示例 2：
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 示例 3：
# 输入：m = 7, n = 3
# 输出：28
# 示例 4：
# 输入：m = 3, n = 3
# 输出：6
# 提示：
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 109
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        print()
        for i in range(1, m):
            for j in range(1, n):
                print(i,j)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                print(dp)
        print(dp)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

#
# sol = Solution()
# sol.uniquePaths(m = 7, n = 3)


# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for j in range(1, m):
            grid[j][0] = grid[j-1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]


# sol = Solution()
# sol.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# sol.minPathSum(grid = [[1,2,3],[4,5,6]])
#
#
# 63. 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 示例 1：
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 示例 2：
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
# 提示：
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        mark = 0

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                mark = 1
            if mark == 1:
                dp[i][0] = 0
        mark = 0
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                mark = 1
            if mark == 1:
                dp[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# 降维

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
                    dp[j] += dp[j - 1]
        return dp[-1]


# sol = Solution()
# sol.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]])

# sol.uniquePathsWithObstacles(obstacleGrid = [[0],[1]])

# 120. 三角形最小路径和
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
# 示例 1：
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 示例 2：
# 输入：triangle = [[-10]]
# 输出：-10
# 提示：
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
# 进阶：
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
# 从上往下，原地修改
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j == i:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        return min(triangle[-1])

# 空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)

# 从下往上，原地修改
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
                print(triangle)
        return triangle[0][0]

# sol = Solution()
# sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]])




# 221. 最大正方形
# 在一个由
# '0'
# 和
# '1'
# 组成的二维矩阵内，找到只包含
# '1'
# 的最大正方形，并返回其面积。
# 示例
# 1：
# 输入：matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# 输出：4
# 示例
# 2：
# 输入：matrix = [["0", "1"], ["1", "0"]]
# 输出：1
# 示例
# 3：
# 输入：matrix = [["0"]]
# 输出：0
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j]
# 为
# '0'
# 或
# '1'


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, column = len(matrix), len(matrix[0])
        dp = [[0] * column for i in range(row)]

        side = 0
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                side = max(side, dp[i][j])
        return side * side

s = Solution()
s.maximalSquare(matrix =
[["1","1","1","1","0"],
 ["1","1","1","1","0"],
 ["1","1","1","1","1"],
 ["1","1","1","1","1"],
 ["0","0","1","1","1"]])









































