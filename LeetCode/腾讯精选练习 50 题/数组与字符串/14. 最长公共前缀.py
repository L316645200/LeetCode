#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 14. 最长公共前缀.py
# @Author: Lin
# @Date  : 2022/4/30 16:09

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 提示：
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
from typing import List


class Solution:
    def longestCommonPrefix(self, l: List[str]) -> str:
        if not l:
            return ""
        length, count = len(l[0]), len(l)

        for i in range(length):
            c = l[0][i]
            if any([i == len(l[j]) or l[j][i] != c for j in range(1, count)]):
                return l[0][:i]
        return l[0]

s = Solution()
res = s.longestCommonPrefix(["a"])
print(res)