#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20231219_1901. 寻找峰值 II.py
# @Author  ：Lin
# @Date    ：2023/12/19 10:40


"""一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。

给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 mat[i][j] 并 返回其位置 [i,j] 。

你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。

要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法





示例 1:



输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3 和 4 都是峰值，所以[1,0]和[0,1]都是可接受的答案。
示例 2:



输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30 和 32 都是峰值，所以[1,1]和[2,2]都是可接受的答案。


提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
任意两个相邻元素均不相等."""
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            max_v, idx = 0, 0
            for i in range(n):
                if mat[mid][i] > max_v:
                    max_v = mat[mid][i]
                    idx = i

            if mid > 0 and mat[mid][idx] < mat[mid-1][idx]:
                high = mid - 1
                continue
            if mid < m - 1 and mat[mid][idx] < mat[mid+1][idx]:
                low = mid + 1
                continue
            return [mid, idx]


