#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File    ：20250128_119. 杨辉三角 II[easy].py
# @Author  ：Lin
# @Date    ：2025/2/5 17:06
"""119. 杨辉三角 II

给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: rowIndex = 3
输出: [1,3,3,1]

示例 2:
输入: rowIndex = 0
输出: [1]

示例 3:
输入: rowIndex = 1
输出: [1,1]

提示:
	0 <= rowIndex <= 33
进阶：
你可以优化你的算法到 O(rowIndex) 空间复杂度吗？


https://leetcode.cn/problems/pascals-triangle-ii/description/?envType=daily-question&envId=2025-01-28"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] * (rowIndex + 1)
        for i in range(rowIndex+1):
            for j in range(i - 1, 0, -1):
                dp[j] += dp[j-1]
        return dp

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
        return row


s = Solution()
s.getRow(rowIndex = 5)
