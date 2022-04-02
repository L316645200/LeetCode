#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 矩阵置零.py
# @Author: Lin
# @Date  : 2021/7/24 11:59
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    r.append([i, j])
        for i,j in r:
            for _ in range(len(matrix[i])):
                matrix[i][_] = 0
            for _ in range(len(matrix)):
                matrix[_][j] = 0


s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])