#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 8 天.py
# @Author: Lin
# @Date  : 2023/6/17 10:55

# 240. 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例 1：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true
# 示例 2：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -109 <= target <= 109
import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < n and row[idx] == target:
                return True
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            print(i,j, matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


s = Solution()
s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)

# 275. H 指数 II
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
# 请你设计并实现对数时间复杂度的算法解决此问题。
# 示例 1：
# 输入：citations = [0,1,3,5,6]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
#      由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
# 示例 2：
# 输入：citations = [1,2,100]
# 输出：2
# 提示：
# n == citations.length
# 1 <= n <= 105
# 0 <= citations[i] <= 1000
# citations 按 升序排列


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


s = Solution()
s.hIndex(citations = [0])
print()
s.hIndex(citations = [0,1,3,5,6])
