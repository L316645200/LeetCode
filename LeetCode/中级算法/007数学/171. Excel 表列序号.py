#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 171. Excel 表列序号.py
# @Author: Lin
# @Date  : 2022/4/13 15:15
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
# 例如：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# 示例 1:
# 输入: columnTitle = "A"
# 输出: 1
# 示例 2:
# 输入: columnTitle = "AB"
# 输出: 28
# 示例 3:
# 输入: columnTitle = "ZY"
# 输出: 701
# 提示：
# 1 <= columnTitle.length <= 7
# columnTitle 仅由大写英文组成
# columnTitle 在范围 ["A", "FXSHRXW"] 内
from functools import reduce


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = ord(columnTitle[0]) - 64
        for c in columnTitle[1:]:
            res = res * 26 + ord(c) - 64
        return res

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda x,y: x*26+y, [ord(_)-64 for _ in list(columnTitle)])

sol = Solution()
sol.titleToNumber("ZY")