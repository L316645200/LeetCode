#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 74. 搜索二维矩阵.py
# @Author: Lin
# @Date  : 2022/7/7 16:07

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


# 二分
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            x, y = divmod(mid, n)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right -= 1
        return False
# O(logmn)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right -= 1
            else:
                left += 1
        k = right
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] > target:
                right -= 1
            else:
                left += 1
        return False
# O(logm+logn) = O(logmn)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = 0, len(matrix[0]) - 1
        while m < len(matrix) and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False

# O(m+n)


s = Solution()
# r = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
r = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)

print(r)