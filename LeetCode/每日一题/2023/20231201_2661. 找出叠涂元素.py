#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231201_2661. 找出叠涂元素.py
# @Author  ：Lin
# @Date    ：2023/12/6 16:08


"""给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。

从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。

请你找出 arr 中第一个使得 mat 的某一行或某一列都被涂色的元素，并返回其下标 i 。



示例 1：

image explanation for example 1
输入：arr = [1,3,4,2], mat = [[1,4],[2,3]]
输出：2
解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。
示例 2：

image explanation for example 2
输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
输出：3
解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。


提示：

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
arr 中的所有整数 互不相同
mat 中的所有整数 互不相同"""
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ep = {}
        for i in range(m):
            for j in range(n):
                ep[mat[i][j]] = [i, j]
        row, line = [0] * m, [0] * n

        for index, k in enumerate(arr):
            i, j = ep[k]
            row[i] += 1
            line[j] += 1
            if row[i] == n or line[j] == m:
                return index


s = Solution()
# s.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]])

s.firstCompleteIndex(arr = [1,4,5,2,6,3], mat = [[4,3,5],[1,2,6]])