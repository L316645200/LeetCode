#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 杨辉三角.py
# @Author: Lin
# @Date  : 2021/7/10 11:55
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# 相关标签
# 数组
# 006动态规划
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        for i in range(1, numRows+1):
            t = []
            for j in range(1, i+1):
                if j == 1 or j == i:
                    t.append(1)
                else:
                    t.append(m[j-2]+m[j-1])
            m = t
            r.append(m)
        return r