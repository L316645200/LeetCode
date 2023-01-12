#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 22. 括号生成.py
# @Author: Lin
# @Date  : 2022/2/22 16:03
# 22. 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
# 输入：n = 1
# 输出：["()"]
# 提示：
# 1 <= n <= 8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s, left, right):
            if right > left or left > n:
                return
            if len(s) == 2 * n:
                ans.append(s)
                return
            dfs(s + "(", left+1, right)
            dfs(s + ")", left, right+1)

        dfs("", 0, 0)
        return ans

