#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 4 天 数组.py
# @Author: Lin
# @Date  : 2022/10/20 17:03

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
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        i, j = n, 0
        while i >= 0 and j <= m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False


s = Solution()
r = s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)


# 435. 无重叠区间
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
# 示例 1:
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 提示:
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        arr = [intervals[0]]
        ans = 0
        for interval in intervals[1:]:
            if arr[-1][1] > interval[0]:
                if arr[-1][1] >= interval[1]:
                    arr[-1] = interval
                ans += 1
            else:
                arr.append(interval)
        return ans

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                if curr[1] >= intervals[i][1]:
                    curr = intervals[i]
                ans += 1
            else:
                curr = intervals[i]
        print(ans)
        return ans


s = Solution()
s.eraseOverlapIntervals(intervals = [[2,5],[1,2],[2,3],[3,4],[1,3]])

print()

s.eraseOverlapIntervals(intervals = [ [1,2], [2,3] ])

















