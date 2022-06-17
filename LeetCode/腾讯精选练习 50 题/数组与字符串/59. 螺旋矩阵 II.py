#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 59. 螺旋矩阵 II.py
# @Author: Lin
# @Date  : 2022/5/3 17:30

# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 示例 1：
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 示例 2：
#
# 输入：n = 1
# 输出：[[1]]
# 提示：
# 1 <= n <= 20
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        mark = [[0]*n for _ in range(n)]
        mark[0][0] = 1
        total = n * n
        current = [0, 0]
        m, rem = 0, 0

        for i in range(1, total):
            r, c = current[0] + directions[rem][0], current[1] + directions[rem][1]
            if not (0 <= r < n) or not (0 <= c < n) or mark[r][c] > 0:
                m += 1
                rem = m % 4
                r, c = current[0] + directions[rem][0], current[1] + directions[rem][1]

            current = [r, c]
            mark[current[0]][current[1]] = i + 1
        return mark



s = Solution()
s.generateMatrix(4)



